---
layout: archive
title: "About Me"
permalink: /
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

## About Me

I am a software engineer with a strong background in distributed systems and database technologies. Currently pursuing a Master's degree in Software Engineering at the University of Science and Technology of China, I have hands-on experience in developing and optimizing distributed storage systems, database internals, and big data processing frameworks. My professional journey includes internships at PingCAP and ByteDance, where I contributed to TiDB ecosystem projects and block storage systems. I also participated in Google Summer of Code, working on PostgreSQL extensions. With a solid foundation in computer science from Hangzhou Dianzi University, I am passionate about building reliable, efficient, and scalable software systems.

Education
======
* 2020.9-2024.6 M.S. University of Science and Technology of China, Software Engineering
* 2016.9-2020.6 B.S. Hangzhou Dianzi University, Computer Science and Technology

Work experience
======
* TiDB Ecosystem Intern PingCAP 2022.5 – 2022.8
  * Supported TiSpark to insert data using Insert SQL. PR2471
  * Added permission validation to TiSpark's DataSource API. PR2366
  * Reproduced, diagnosed and fixed a bug that could cause data loss. PR2433

* Block Storage Intern ByteDance 2021.8 – 2022.3
  * Completed the design of Exactly-Once semantics based on existing theory in the original architecture
  * Participated in developing Extent CRC validation, improved end-to-end CRC checking, and provided rich debugging information
  * Coordinated externally to decommission three old version clusters, reducing maintenance costs

* PostgreSQL-pg_systat Google Summer of Code 2021.6 – 2021.8
  * Added pg_stat_statements, pg_stat_progress_cope, and pg_buffercache panels
  * Increased database version and extension installation status checks, backward compatibility, and reduced unnecessary queries

Related Experience
======
* TinyKV TiDB Talent Project
  * Implemented the Raft algorithm for synchronizing server-side data
  * Implemented support for adding/removing nodes, splitting regions, and load balancing
  * Implemented distributed transactions based on MVCC and Percolator algorithms

* CMU15-445 Course Projects
  * Implemented Buffer Pool replacement using Clock algorithm
  * Implemented database index based on Hashtable
  * Implemented ARISE algorithm for database crash recovery