
<div align="center">
   <h1>🧊 Inferring Europa’s Ice Rheology from Surface Roughness</h1>
   <b>A planetary geoscience analysis using Galileo SSI imagery</b>
</div>

---

## Overview

This project investigates the surface roughness of <b>Europa</b>, one of Jupiter’s moons, to infer the rheological (mechanical) properties of its ice shell. By analyzing high-resolution Galileo SSI global mosaic images, we quantify roughness across different terrain types—<b>smooth plains</b>, <b>lineae</b>, and <b>chaos regions</b>—and interpret these differences in terms of ice deformation, thermal history, and subsurface processes.

---

## Scientific Motivation

Europa’s surface displays a striking diversity of terrains, from smooth, resurfaced plains to fractured, chaotic regions. These morphologies record the moon’s ice shell mechanics and thermal evolution. Quantifying surface roughness provides insight into the underlying ice rheology, helping to answer:

<ul>
   <li>Why are some regions smooth while others are fractured or chaotic?</li>
   <li>What does this tell us about the temperature, viscosity, and deformation style of Europa’s ice shell?</li>
</ul>

---

## Project Structure

<ul>
   <li><b>Europa_Ice_Rheology_Surface_Roughness.ipynb</b>: Main Jupyter notebook for data loading, ROI selection, roughness quantification, comparative analysis, and scientific interpretation.</li>
   <li><b>download_europa_mosaics.py</b>: Script to download Galileo SSI Europa global mosaic images from AWS Open Data.</li>
   <li><b>/data/</b>: Directory containing downloaded Galileo SSI images (GeoTIFF or equivalent).</li>
</ul>

---

## Workflow

<ol>
   <li><b>Data Acquisition</b><br>
      Download Galileo SSI Europa global mosaic images using the provided script or manually from <a href="https://registry.opendata.aws/planets/">NASA PDS/AWS Open Data</a>.<br>
      Place images in the <code>/data</code> directory.
   </li>
   <li><b>Data Loading & Preprocessing</b><br>
      Load images using <code>rasterio</code> or <code>skimage</code>.<br>
      Convert to grayscale, normalize illumination, and rescale pixel values for consistent analysis.
   </li>
   <li><b>Region of Interest (ROI) Selection</b><br>
      Manually or programmatically select ROIs representing different terrain types (smooth plains, lineae, chaos terrain).<br>
      Ensure consistent ROI size and scale for fair comparison.
   </li>
   <li><b>Surface Roughness Quantification</b><br>
      Compute roughness metrics for each ROI:
      <ul>
         <li>Local standard deviation (variance)</li>
         <li>RMS roughness</li>
         <li>Texture entropy (Shannon entropy)</li>
         <li>Power spectral density (PSD) via FFT</li>
      </ul>
      Aggregate results across all images and terrain types.
   </li>
   <li><b>Comparative Analysis & Visualization</b><br>
      Visualize roughness metrics using boxplots and log–log PSD curves.<br>
      Compare terrain types and discuss physical implications.
   </li>
   <li><b>Physical Interpretation</b><br>
      Link observed roughness to ice rheology:
      <ul>
         <li>Low roughness: Viscous relaxation, warm/ductile ice</li>
         <li>High roughness: Brittle deformation, recent resurfacing</li>
      </ul>
      Discuss temperature-dependent viscosity and implications for Europa’s subsurface.
   </li>
   <li><b>Limitations & Scientific Integrity</b><br>
      Discuss limitations due to illumination, image resolution, ROI selection, and lack of direct rheological measurements.<br>
      Emphasize qualitative interpretation and scientific rigor.
   </li>
</ol>

---

## Requirements

- Python 3.8+
- Recommended: virtual environment (venv)
- Required packages:
   - numpy
   - matplotlib
   - scikit-image
   - rasterio
   - pandas
   - boto3 (for image download script)
   - imagecodecs (for some GeoTIFFs)

<details>
<summary><b>Install dependencies</b></summary>

```bash
pip install numpy matplotlib scikit-image rasterio pandas boto3 imagecodecs
```

</details>

---

## Data Sources

- <b>Galileo SSI Europa Global Mosaic</b>: <a href="https://pds-imaging.jpl.nasa.gov/volumes/galileo.html">NASA PDS Imaging Node</a>
- <b>AWS Open Data Registry</b>: <a href="https://registry.opendata.aws/planets/">Europa Mosaics</a>

---

## Usage

1. Clone this repository and set up a Python environment.
2. Download Galileo SSI images using <code>download_europa_mosaics.py</code> or manually, and place them in <code>/data</code>.
3. Open <code>Europa_Ice_Rheology_Surface_Roughness.ipynb</code> in Jupyter and run all cells.
4. Review and interpret the results, adjusting ROI coordinates or analysis parameters as needed.

---

## Figures & Results

- All plots are generated in the notebook, including:
   - Example ROIs for each terrain type
   - Boxplots of roughness metrics
   - Mean ± std PSD curves (log–log) for each terrain type
- Figures can be saved for publication by uncommenting the relevant lines in the notebook.

---

## Limitations

- Illumination effects and image artifacts may bias roughness metrics.
- Manual ROI selection introduces subjectivity.
- Image resolution limits the smallest measurable roughness scales.
- All rheological inferences are qualitative.

---

## Acknowledgments

- NASA Galileo SSI Team
- NASA PDS Imaging Node
- AWS Open Data Registry

---

## License

This project is released under the MIT License. See <code>LICENSE</code> for details.
