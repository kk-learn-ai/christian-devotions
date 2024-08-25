# Christian Devotions Project

## Overview
This project implements a modular system for publishing Christian daily devotions using the crewAI library. The system is designed to streamline the process of creating, editing, and managing inspirational content to encourage readers in their faith journey.

## Folder Structure
```
christian-devotions
├── content_creation/
│ ├── lead_writer/
│ ├── supporting_writers/
│ └── biblical_scholar/
├── editorial/
│ ├── managing_editor/
│ ├── copy_editor/
│ └── fact_checker/
├── project_management/
│ ├── project_manager/
│ └── legal_advisor/
├── config/
│ ├── devotional_config.yml
└── README.md
```

## Module Descriptions

### Content Creation
Responsible for developing inspiring and theologically sound devotional content tailored to specific audience needs.

### Editorial
Oversees the refinement and quality assurance of devotional content, ensuring clarity, consistency, and audience-appropriate language.

### Project Management
Facilitates coordination among teams and proposes web publication timeline for devotional content upon completion of content creation, editorial review, and social media preparation.

## Configuration
Agent configurations and tasks are defined in a single YAML file located in the `config/` directory:
- `devotional_config.yml`: Defines roles, goals, backstories, and tasks for each agent in the system.

## Key Features
- Dynamic theme selection: The Project Manager asks the user for the theme of each devotional series.
- Audience-focused content: Content is tailored to specific target audiences identified through brainstorming.
- Collaborative workflow: Cross-team collaboration is facilitated to ensure cohesive and high-quality devotional content.
- Flexible publication timeline: The Project Manager suggests publication timelines based on team progress and standard durations.

## Usage
[Include instructions on how to run the project, dependencies, etc.]

## Contributing
[Include guidelines for contributing to the project]

## License
This project is licensed under the MIT License. 

The MIT License is a permissive license that allows for reuse of this software in proprietary projects provided the license text is included. It's simple and compatible with many other licenses, making it ideal for open source projects.

Key points of the MIT License:
- You can use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software.
- You must include the copyright notice and the LICENSE file in all copies or substantial portions of the software.
- The software is provided "as is", without warranty of any kind.

