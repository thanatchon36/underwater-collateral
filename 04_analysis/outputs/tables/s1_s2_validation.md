<!-- Optical (Sentinel-2 L2A SCL) check of the Sentinel-1 rule, RQ1 2024 radar sample. Observed = at least one scene with >= 50% clear pixels in both 2023 and 2024 (15 Aug - 31 Oct). Optically flooded = largest 2024 water share minus largest 2023 water share > 0.1. For treated sheets the share is a lower bound on precision; for controls it is a contamination rate. 0 scene reads failed. Sources: Copernicus Sentinel-2 L2A via Microsoft Planetary Computer; author's calculations. -->

| group   | province      |   sheets |   observed |   share_optically_flooded |   median_new_water |
|:--------|:--------------|---------:|-----------:|--------------------------:|-------------------:|
| control | chiang-rai    |      495 |        495 |                     0.006 |              0     |
| control | nakhon-phanom |      981 |        981 |                     0.003 |              0     |
| control | nong-khai     |      333 |        333 |                     0.054 |              0     |
| control | phayao        |       82 |         82 |                     0     |              0     |
| treated | chiang-rai    |       88 |         88 |                     0.568 |              0.143 |
| treated | nakhon-phanom |       25 |         25 |                     0.88  |              0.311 |
| treated | nong-khai     |       60 |         60 |                     0.783 |              0.465 |
| treated | phayao        |       25 |         25 |                     0.64  |              0.282 |
| control | all           |     1891 |       1891 |                     0.013 |              0     |
| treated | all           |      198 |        198 |                     0.682 |              0.246 |
