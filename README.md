# 🧪 Chemistry Inventory Management System


**Assessment 2 — Mini Project**

A Python-based inventory management application designed to modernise the University Chemistry Department's legacy inventory system by consolidating inconsistent reagent and laboratory equipment data into a unified, maintainable solution.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python\&logoColor=white)
![JSON](https://img.shields.io/badge/Data-JSON-000000?logo=json\&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)
![Project](https://img.shields.io/badge/Project-Academic%20Assessment-6C63FF)

---

## 📋 Table of Contents

* [Overview](#-overview)
* [Project Objectives](#-project-objectives)
* [Key Features](#-key-features)
* [Technology Stack](#-technology-stack)
* [Project Structure](#-project-structure)
* [Data Migration](#-data-migration)
* [Object-Oriented Design](#-object-oriented-design)
* [Reporting Features](#-reporting-features)
* [Team Contributions](#-team-contributions)
* [Assessment Information](#-assessment-information)
* [License](#-license)

---

## 🔬 Overview

The Chemistry Department's original inventory system consists of multiple legacy files with inconsistent formats, missing values, duplicate records, and differing data structures.

This project aims to replace that fragmented system with a unified Python application that can:

* Analyse and clean the existing inventory data.
* Migrate reagent and equipment records into a consistent JSON structure.
* Manage inventory items through an object-oriented model.
* Load and save inventory data reliably.
* Generate useful inventory reports using functional programming techniques.

The application is being developed collaboratively using Git and GitHub, with individual contributions tracked through version control.

## 🎯 Project Objectives

The primary objectives of this project are to:

1. **Analyse legacy data** — Identify inconsistencies, formatting issues, missing values, and duplicate records.
2. **Design a unified schema** — Establish a consistent JSON structure for reagents and laboratory equipment.
3. **Implement data migration** — Build a migration script that cleans, normalises, and consolidates the original datasets.
4. **Apply object-oriented programming** — Develop reusable classes and an inventory management system.
5. **Implement persistence** — Support reliable loading and saving of inventory data.
6. **Develop functional reporting** — Use appropriate functional programming constructs to produce useful inventory reports.
7. **Maintain code quality** — Follow modular design principles and use Git checkpoints to document development.

## ✨ Key Features

*Planned features — implementation status will be updated as development progresses.*

| Feature               | Description                                        | Status     |
| --------------------- | -------------------------------------------------- | ---------- |
| Legacy data analysis  | Identify structural and formatting inconsistencies | 🟡 Planned |
| Unified JSON schema   | Standardise reagent and equipment records          | 🟡 Planned |
| Data migration        | Clean and migrate both legacy datasets             | 🟡 Planned |
| Duplicate handling    | Identify and merge duplicate records appropriately | 🟡 Planned |
| Object-oriented model | Represent inventory items using reusable classes   | 🟡 Planned |
| Inventory management  | Manage items in memory using suitable collections  | 🟡 Planned |
| JSON persistence      | Load inventory data and save changes               | 🟡 Planned |
| Functional reporting  | Generate reports using functional programming      | 🟡 Planned |

> Update the status labels as each feature is implemented and tested.

## 🛠️ Technology Stack

| Technology | Purpose                                    |
| ---------- | ------------------------------------------ |
| Python     | Core application logic and data processing |
| JSON       | Unified inventory storage format           |
| CSV        | Source format for legacy reagent records   |
| Git        | Version control and checkpoint tracking    |
| GitHub     | Shared repository and team collaboration   |

## 📁 Project Structure

The repository is expected to follow this structure:

```text
chemistry-inventory-management/
│
├── legacy_inventory.csv    # Legacy reagent dataset
├── legacy_equipment.json   # Legacy equipment dataset
│
├── migrate.py              # Data cleaning and migration
├── app.py                  # Object-oriented inventory application
├── inventory.json          # Unified inventory data
│
├── README.md               # Project documentation and report
└── .gitignore              # Files excluded from version control
```

*The structure may be adjusted as the project develops. The legacy files should be included only where permitted by the assessment requirements.*

## 🔄 Data Migration

The `migrate.py` script is responsible for transforming the supplied legacy datasets into a single, consistent JSON inventory.

The migration process is intended to cover:

* Reading the CSV and JSON source files.
* Normalising field names, casing, and data formats.
* Cleaning and standardising dates and quantities.
* Validating and standardising reagent identifiers.
* Handling missing or invalid values consistently.
* Identifying and merging duplicate records according to documented rules.
* Exporting the final unified dataset to `inventory.json`.

The migration rules and unified schema will be documented in the project report.

## 🏗️ Object-Oriented Design

The main application, `app.py`, will use an object-oriented architecture to represent and manage inventory items.

The planned design includes:

* **`InventoryItem`** — An abstract base class defining the common interface and attributes shared by all inventory items.
* **`Reagent`** — A subclass representing chemical reagents and their specific attributes.
* **`Equipment`** — A subclass representing laboratory equipment and its specific attributes.
* **`InventoryManager`** — A class responsible for managing inventory collections, loading data, saving changes, and coordinating inventory operations.

This structure is intended to demonstrate abstraction, inheritance, encapsulation, and polymorphism while keeping the application modular and maintainable.

## 📊 Functional Reporting Features

The application will include two functional reporting methods designed to demonstrate appropriate use of functional programming concepts.

Potential techniques include:

* **Filtering:** Selecting inventory records that match particular conditions.
* **Mapping:** Transforming inventory data into a report-friendly representation.
* **Sorting:** Ordering records by relevant attributes.
* **Lambda expressions:** Defining concise functions for sorting and filtering.
* **Higher-order functions:** Passing functions into operations that process inventory collections.

The final reporting features will be documented here once the implementation and requirements have been confirmed.

## 👥 Team Contributions

This project is a collaborative assessment. Each member's contribution will be evidenced through the Git commit history and documented in the final report.

| Team Member | Responsibilities | GitHub Profile                          |
| ----------- | ---------------- | --------------------------------------- |
| Riker       | To be confirmed  | [GitHub](https://github.com/Riker-Hoch) |
| Member 2    | To be confirmed  | [GitHub](https://github.com/)           |
| Member 3    | To be confirmed  | [GitHub](https://github.com/)           |
| Member 4    | To be confirmed  | [GitHub](https://github.com/)           |

*Replace the example rows with your actual team members, assigned tasks, and profile links. Ensure the task-distribution list matches the commit history.*

## 🎓 Assessment Information

**Assessment:** Assessment 2 — Mini Project
**Course:** Applied Information Technology
**Project Domain:** Chemistry Inventory Management
**Primary Language:** Python

### Learning Outcomes

This project addresses the following learning outcomes:

* **LO1:** Apply advanced object-oriented programming concepts to build modular, maintainable, and reusable software.
* **LO2:** Select suitable data collections to manage and manipulate inventory data.
* **LO3:** Apply functional programming constructs, including anonymous and higher-order functions.
* **LO4:** Apply appropriate persistence strategies for consistent and reliable data management.

### Submission Requirements

The final submission must include:

* `migrate.py` — Data migration script.
* `app.py` — Main application code.
* `inventory.json` — Generated unified inventory dataset.
* `README.md` — Completed group report.
* Git commit history — Evidence of individual contributions and required development checkpoints.

## 📄 License

This project was created for educational purposes as part of an academic assessment.

A formal open-source licence has not yet been specified. No reuse or redistribution terms should be assumed until a licence is selected.

---

<p align="center">
  <sub>Developed collaboratively with Python, object-oriented programming, functional programming, and Git.</sub>
</p>
