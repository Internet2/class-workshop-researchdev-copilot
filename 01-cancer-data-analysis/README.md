# Cancer Data Analysis Notebook

This repository contains a collection of notebooks for the data analysis workflow of cancer data. The notebooks cover various stages of the analysis, including data exploration, processing, and visualization.

## Notebooks

- [`fm-ad-notebook-exploration.ipynb`](fm-ad-notebook-exploration.ipynb): This notebook focuses on exploring the cancer data, performing initial data exploration, and gaining insights into the dataset.

- [`fm-ad-notebook-processing.ipynb`](fm-ad-notebook-processing.ipynb): This notebook covers the data processing steps, including cleaning, transforming, and preparing the data for further analysis.

- [`fm-ad-notebook-visualization.ipynb`](fm-ad-notebook-visualization.ipynb): This notebook focuses on visualizing the processed data, creating informative plots, charts, and graphs to communicate the findings effectively.

## Getting started

To get started with the cancer data analysis, follow these steps:

1. Ensure you have cloned the repository by following the steps in the [Getting Started section of the main README](../README.md#getting-started) of this repo.
2. Open the notebooks in Visual Studio Code.
3. Run the notebooks in the specified order (exploration, processing, visualization) to perform the complete data analysis workflow.

## Additional information about the dataset

### Study Summary
The dataset we will be working with was used in the publication titled ["High-Throughput Genomic Profiling of Adult Solid Tumors Reveals Novel Insights into Cancer Pathogenesis."](https://aacrjournals.org/cancerres/article/77/9/2464/625134/High-Throughput-Genomic-Profiling-of-Adult-Solid) This paper analyzed genomic data from 18,004 unique adult solid tumors. The focus was on integrating this large-scale data to uncover novel molecular alterations, explore disease specificity, and identify potential therapeutic targets across various cancer types. The study compared the genomic profiles of these tumors to existing databases like The Cancer Genome Atlas (TCGA) and identified differences in alteration frequencies, especially in breast and lung cancers where there seems to be an enrichment of treatment-refractory samples.

Overall, the study illustrates the power of large-scale genomic profiling in identifying unique and clinically relevant genomic alterations that may inform precision medicine approaches and treatment options.

### Column Descriptions

In spirit of this workshop, GitHub Copilot was used to describe a general interpretation of the columns of the dataset.

Here is the prompt that was used:
```
Explain what columns below mean in terms of genomic research. Group columns if they serve a similar role or belong in a similar group.

*The column names were included in the original prompt, but removed from here for the sake of brevity*
```


Below is the output from GitHub Copilot:

```
Case Information:
1. cases.submitter_id: The ID assigned by the submitter for the case.
2. case_id: Unique identifier for each patient or case.
3. project_id: The ID of the project under which the genomic profiling was conducted.
4. project.name: The name of the project.
5. cases.disease_type: The type of disease the patient is diagnosed with.
6. cases.primary_site: The primary location in the body where the disease originated.

Demographic Information:
7. demographic.submitter_id: The ID assigned by the submitter for the demographic data.
8. demographic_id: Unique identifier for the demographic data.
9. demographic.gender: The gender of the patient.

Diagnosis Information:
10. diagnoses.submitter_id: The ID assigned by the submitter for the diagnosis.
11. diagnosis_id: Unique identifier for the diagnosis.
12. diagnoses.primary_diagnosis: The primary diagnosis made for the patient.
13. diagnoses.site_of_resection_or_biopsy: The site in the body from where the tissue sample was taken for biopsy.
14. diagnoses.classification_of_tumor: The classification of the tumor, which could include information about its malignancy, cell type, etc.
15. diagnoses.tissue_or_organ_of_origin: The tissue or organ where the disease or condition originated.
16. diagnoses.age_at_diagnosis: The age of the patient when they were first diagnosed.
17. diagnoses.morphology: The structure and form of the disease or condition at a microscopic level.

Sample Information:
18. samples.submitter_id: The ID assigned by the submitter for the sample.
19. sample_id: Unique identifier for the sample. 20. samples.sample_type: The type of sample taken for genomic profiling, such as blood, tissue, etc.
21. samples.tumor_descriptor: A descriptor for the tumor sample, which could include information about its stage, size, etc.

Aliquot Information:
22. aliquots.submitter_id: The ID assigned by the submitter for the aliquot.
23. aliquot_id: Unique identifier for the aliquot.
24. aliquots.analyte_type: The type of analyte in the aliquot (portion of a sample), such as DNA, RNA, etc.

Slide Information:
25. slides.submitter_id: The ID assigned by the submitter for the slide.
26. slide_id: Unique identifier for the slide.
27. slides.percent_tumor_nuclei: The percentage of nuclei in the slide that are tumor cells.

Read Group Information:
28. read_groups.submitter_id: The ID assigned by the submitter for the read group.
29. read_group_id: Unique identifier for the read group.
30. read_groups.is_paired_end: A boolean indicating whether the sequencing was done with paired-end reads, which can provide more accurate and complete data.
31. read_groups.library_name: The name of the library where the genomic data is stored.
32. read_groups.library_selection: The method used to select the library.
33. read_groups.library_strategy: The strategy used for sequencing the library.
34. read_groups.platform: The platform used for sequencing, such as Illumina, PacBio, etc.
35. read_groups.sequencing_center: The center where the sequencing was performed.
36. read_groups.name: The name of the read group, which is a set of reads that were generated from the same run.
37. read_groups.read_length: The length of the reads generated from sequencing.
38. read_groups.experiment_name: The name of the experiment under which the sequencing was performed.

Please note that these are general interpretations and the exact meaning could vary based on the specifics of your research project or dataset.
```

## Contributing

If you would like to contribute to this project, feel free to submit a pull request. We welcome any improvements, bug fixes, or additional analysis notebooks.