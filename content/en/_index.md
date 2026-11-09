---
title: High-Energy Astrophysics Lab
type: landing

sections:
  # ===== Hero =====
  - block: hero-rotator
    id: hero
    content:
      title: High-Energy Astrophysics Lab
      text: |
        From the extreme environments around black holes to the radiation environment on the lunar surface —
        we tackle the mysteries of the high-energy universe through theory and multi-messenger observations
        (X-rays, MeV gamma rays, radio, neutrinos, and gravitational waves).
      primary_action:
        text: Join Us
        url: join/
      secondary_action:
        text: Explore Our Research
        url: research/
      images:
        - file: hero/corona.jpg
          credit: "Credit: RIKEN"
        - file: hero/fermi.jpg
          credit: "Credit: NASA/DOE/Fermi LAT Collaboration"
        - file: hero/m51.jpg
          credit: "Credit: NASA/ESA/STScI"
        - file: hero/moon.jpg
          credit: "Credit: NASA"
    design:
      spacing:
        padding: ['0', '0']

  # ===== Research (two categories) =====
  - block: research-areas
    id: research
    content:
      title: Research
      text: From fundamental astrophysics to applied radiation science.
      groups:
        - title: Fundamental Astrophysics
          kicker: 01 — FUNDAMENTAL
          accent: navy
          description: Uncovering the physics of the high-energy universe — black holes and MeV gamma rays — through theory and multi-messenger observations.
          cta:
            text: Explore fundamental research
            url: research/#fundamental
          items:
            - name: Black Hole Astrophysics
              icon: star
              gradient: from-gray-700 to-slate-900
              description: Magnetic field measurements and origin of AGN coronae, jet launching, accretion physics, and extreme physics near the event horizon.
              topics: [AGN coronae, X-ray polarimetry, ALMA, XRISM]
              cta:
                text: Read more
                url: research/#blackhole
            - name: High-Energy Astrophysics (MeV)
              icon: bolt
              gradient: from-purple-500 to-fuchsia-600
              description: Pioneering MeV gamma-ray astronomy and multi-messenger studies.
              topics: [GRAMS, neutrinos, blazars]
              cta:
                text: Read more
                url: research/#mev
        - title: Applied High-Energy and Radiation Studies
          kicker: 02 — APPLIED
          accent: gold
          description: Applying our expertise in high-energy astrophysics to real-world radiation challenges of the space age.
          cta:
            text: Explore applied research
            url: research/#applied
          items:
            - name: Lunar Radiation Environment
              icon: moon
              gradient: from-amber-400 to-yellow-600
              description: Understanding and forecasting the cosmic-ray and radiation environment on the lunar surface for the era of human lunar activity.
              topics: [cosmic rays, solar energetic particles, Artemis]
              cta:
                text: Read more
                url: research/#lunar
    design:
      spacing:
        padding: ['2.5rem', '0']

  # ===== News =====
  - block: news-list
    id: news
    content:
      title: News
      count: 5
    design:
      spacing:
        padding: ['2.5rem', '0']

  # ===== Recent Publications =====
  - block: markdown
    id: latest-pubs
    content:
      title: Recent Publications
      text: |
        <!-- RECENT_PUBS:START -->
        - Narita, K., **Inoue, Y.**, Hatsukade, B., Fukazawa, Y. (2026). FALCON (FERMI-ALMA Calibrator ObservatioN): Cross-matching ALMA Calibrators with Fermi-LAT Blazars. *arXiv e-prints*, arXiv:2611.07737. [SciX](https://scixplorer.org/abs/2026arXiv261107737N/abstract) / [arXiv](https://arxiv.org/abs/2611.07737) / [DOI](https://doi.org/10.48550/arXiv.2611.07737)
        - Tsuji, N., Tresoldi, C., Mori, K., Suzuki, H., Lundy, M., et al. (2026). XMM-Newton Resolves Parsec-scale X-ray Jets in the PeVatron Microquasar V4641 Sgr. *arXiv e-prints*, arXiv:2610.02966. [SciX](https://scixplorer.org/abs/2026arXiv261002966T/abstract) / [arXiv](https://arxiv.org/abs/2610.02966) / [DOI](https://doi.org/10.48550/arXiv.2610.02966)
        - Noda, H., Hada, K., Maruyama, H., Kayanoki, T., Toma, K., et al. (2026). Disk Truncation Triggers Relativistic Jet Launching of a Highly Accreting Supermassive Black Hole. *The Astrophysical Journal Letters* 1010, L39. [SciX](https://scixplorer.org/abs/2026ApJ..1010L..39N/abstract) / [arXiv](https://arxiv.org/abs/2609.27057) / [DOI](https://doi.org/10.3847/2041-8213/aeaa2c)
        - Venselaar, S. M., Ricci, C., **Inoue, Y.**, Chang, C., Doi, A., et al. (2026). Nuclear Millimeter Continuum Emission in Radio-Quiet Active Galactic Nuclei: an ALMA Spectral and Variability Study. *arXiv e-prints*, arXiv:2610.30286. [SciX](https://scixplorer.org/abs/2026arXiv261030286V/abstract) / [arXiv](https://arxiv.org/abs/2610.30286) / [DOI](https://doi.org/10.48550/arXiv.2610.30286)
        - Xue, R., **Inoue, Y.**, Wang, Z., Liao, N., Xiong, D. (2026). Locating the Production Sites of High-energy Neutrinos in Blazar Jets. *The Astrophysical Journal Supplement Series* 286, 20. [SciX](https://scixplorer.org/abs/2026ApJS..286...20X/abstract) / [arXiv](https://arxiv.org/abs/2606.02024) / [DOI](https://doi.org/10.3847/1538-4365/ae9286)
        <!-- RECENT_PUBS:END -->
        [All publications →](publication/)
    design:
      spacing:
        padding: ['2.5rem', '0']

  # ===== Join CTA =====
  - block: cta-card
    id: join-cta
    content:
      title: Join Us
      text: We are recruiting graduate students (MSc/PhD), postdocs, and undergraduates. Black holes, gamma rays, neutrinos, or the Moon — if any of these excites you, get in touch.
      button:
        text: How to Join
        url: join/
    design:
      spacing:
        padding: ['2.5rem', '0']
---
