#!/usr/bin/env bash
# =====================================================================
# SciX (ADS) 公開ライブラリ → BibTeX → Hugo Blox 論文ページ自動生成
#
# 前提:
#   - ADS/SciX API トークン(https://scixplorer.org/user/settings/token)
#     を環境変数 ADS_DEV_KEY に設定
#   - pipx install academic  (Hugo Blox の BibTeX インポータ)
#
# 使い方:
#   export ADS_DEV_KEY=xxxxxxxx
#   ./scripts/fetch_publications.sh
# =====================================================================
set -euo pipefail

LIB_ALL="r0HdPWXHQKOV8kUwuZDq5Q"     # 全論文ライブラリ
API="https://api.adsabs.harvard.edu/v1"
WORKDIR="$(mktemp -d)"

# 1. ライブラリ内の bibcode 一覧を取得(ページング対応, 最大2000件)
curl -sf -H "Authorization: Bearer ${ADS_DEV_KEY}" \
  "${API}/biblib/libraries/${LIB_ALL}?rows=2000" \
  | python3 -c "import sys,json; print('\n'.join(json.load(sys.stdin)['documents']))" \
  > "${WORKDIR}/bibcodes.txt"

echo "Found $(wc -l < "${WORKDIR}/bibcodes.txt") bibcodes"

# 2. BibTeX としてエクスポート
python3 - "$WORKDIR" << 'PYEOF'
import json, os, sys, urllib.request
workdir = sys.argv[1]
bibcodes = open(f"{workdir}/bibcodes.txt").read().split()
req = urllib.request.Request(
    "https://api.adsabs.harvard.edu/v1/export/bibtex",
    data=json.dumps({"bibcode": bibcodes}).encode(),
    headers={"Authorization": f"Bearer {os.environ['ADS_DEV_KEY']}",
             "Content-Type": "application/json"})
with urllib.request.urlopen(req) as r:
    open(f"{workdir}/publications.bib", "w").write(json.load(r)["export"])
PYEOF

# 3. Hugo Blox 形式に変換(ja 側に生成 → en 側へ同期)
academic import "${WORKDIR}/publications.bib" content/ja/publication/ --compact
rsync -a --ignore-existing content/ja/publication/ content/en/publication/

echo "Done. Review content/{ja,en}/publication/ and commit."
