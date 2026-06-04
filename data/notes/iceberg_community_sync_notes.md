Iceberg Community Sync Notes
●	This doc has notes from previous Iceberg discussions and agendas for upcoming syncs
●	Please add Agenda items that you’d like to discuss. 
●	Everyone is welcome to attend syncs. Subscribe to this calendar to receive a notification.
●	All current proposals: label:proposal
●	Meeting Recording Uploading Instructions

2026-06-03 (Recording)
●	Highlights
○	Java
■	API, Core, Orc: Implement project() for partition statistics scan API (#16569) <Thanks gaborkaszab!>
■	CI: Make CVE scan blocking on PRs, informational on main (#16287) <Thanks Kevin Liu!>
■	Core, Orc: Remove deprecated partition stats read functionality (#14998) <Thanks gaborkaszab!>
■	Core, Parquet: Allow for Writing Parquet/Avro Manifests in V4 (#15634) <Thanks Russell Spitzer!>
■	Core: Add V4 location relativization utilities (#16174) <Thanks Anoop Johnson!>
■	Core: Cache PartitionData template in PartitionsTable to avoid rebuilding Avro schema per partition (#16208) <Thanks SevenJ!>
■	Core: v4 table metadata location should be optional (#16572) <Thanks Alex Stephen!>
■	Flink: Support UUID type in Avro and Parquet readers and writers (#16097) <Thanks Joy Haldar!>
■	Flink: Support writing shredded variant (#15596) <Thanks GuoYu!>
■	OpenAPI: Add CatalogObjectIdentifier schema (#16144) <Thanks Steven Zhen Wu!>
■	REST Spec: Add unregister table endpoint (#16400) <Thanks Ryan Blue!>
■	Spark: Also disable min/max aggregation push down for binary (#16328) <Thanks Dong Wang!>
■	Spark: Backport Add _row_id and _last_updated_sequence_number raeder in Orc to support lineage (#16534) <Thanks GuoYu!>
■	Spec: Add v4 content stats representation (#14234) <Thanks Eduard Tudenhoefner!>
■	Website: remove duplicated entries from search (#16368) <Thanks Maksim Konstantinov!>
■	[SPEC] Add relative paths to v4 spec (#15630) <Thanks Daniel Weeks!>
○	Python
■	Improve `add_files` duplicate-check performance by streaming manifest entries (Thanks Ben!)
■	Pagination support for REST `list_namespaces` `list_tables` and `list_views`(Thanks Yuya!)
■	Add page-size support for `list_namespaces`, `list_tables`, `list_views` in REST (Thanks Yuya!)
■	Add `View` object API for abstracting view metadata access (Thanks Gabriel!)
■	Add `pa.RecordBatchReader` support in `Table.append`/`overwrite` for streaming writes (Thanks Paul!)
■	Fix `TSaslClientTransport` reuse to eliminate server-side SASL noise (Thanks barking-code!)
■	Fix zero-byte file handling in `FsspecInputFile`/`FsspecOutputFile.__len__` (Thanks Minh!)
○	Rust
■	Add `cargo-public-api` CI checks to catch unintentional breaking API changes (Thanks Xander!)
■	Switch crate publishing to `cargo publish --workspace` to fix missing crates (Thanks blackmwk!)
■	Add encryption step 5: `EncryptionManager` with KEK/DEK envelope encryption (Thanks Xander!)
■	Add Hugging Face storage option to `storage/opendal` README (Thanks Quentin!)
■	Fix `FastAppend` dropping delete-only manifests causing deleted files to reappear (Thanks Liang-Chi!)
■	Add [breaking] support for custom `Runtime` in `Catalog` via `CatalogBuilder::with_runtime` (Thanks Shawn!)
○	Go
■	Improve CLI commands (Thanks Tanmay!)
■	Add golden round-trip tests (Thanks Andrei!)
■	Preserve row lineage through copy-on-write rewrites on v3 tables (Thanks Tanmay!)
■	Add variant type support (Iceberg v3, non-shredding path) (Thanks Neelesh!)
○	Cpp
■	Add `MergingSnapshotUpdate` base for merge-based snapshot operations (Thanks Guotao!)
■	Add position delete coalescing into range inserts with 2–10x speedup (Thanks Sebastian!)
■	Add Puffin file reader and writer with compression support  (Thanks ZhaoXuan!)
■	Add v3 timestamp nanosecond primitive types (Thanks Junwang!)
■	Add delete filter support for merge-on-read data batches (Thanks Gang!)
●	Releases
○	Java 1.10.2 (devlist) and 1.11 (devlist) releases are out
○	Go 0.6.0 release is out! (devlist) (blog)
○	Upcoming releases
■	Java 1.12
●	Release manager: Neelesh
●	1.13 RM: Anurag
■	PyIceberg 0.12.0
■	C++ 0.3.0
■	Iceberg-rust 0.10.0
●	Discussion
○	[Ryan] Test resource consumption
■	Removed Spark 3.4
■	Spark version pruning mail thread - https://lists.apache.org/thread/6kmh92wl6qkw08dpgv04bl51v590phbl
○	[Anu / Yuya] Decouple Iceberg from Hadoop codebase #14284
■	PR https://github.com/apache/iceberg/pull/16588	
○	[Vishal] UUID comparison bug PR now addresses “strict” metrics evaluator gap; open for review #14500
○	[Ryan] Deprecating ORC
○	[Giorgio] Proposal: Capture and emit aggregated data-file (Parquet footer) metrics at commit time (Issue)
○	[Jared] Add DataFusion to overcome OOM issues in bindings (namely Python)
■	Draft Proposal: Support for PyIceberg MoR
○	[Russ] Release Automation - 
○	[Kevin] Iceberg Summit 2027
●	PR to review
○	[Shekhar] PR review - Add multi-snapshot support to SnapshotChanges PR #16224
○	[Mukund] PR review - Core: Enable picking of old partition spec data files using a flag for rewrite #16190
○	[SteveL] Core, Spark: Add JMH benchmarks for Variants #15629
○	[Giorgio] Core: Parallelize RewriteManifests added-manifest copy path #16336


2026-05-13 (Recording) 
●	Highlights
○	Welcome new committer: Shawn Chang & Andrei Tserakhau
○	Iceberg Summit 2026 Selection Committee Retrospective Notes (devlist)
○	Iceberg Summit 2026 video ~coming~
○	Java
■	Licenses / Notices / Dependencies / Bundles <Thanks Blue and Kevin>
■	Remove runtime Jar from build and deploy [#16163] (Thanks Ryan!)
■	Core: Add builders for v4 structs (#16092) <Thanks Anoop Johnson!>
■	Core: Add implementations of v4 TrackedFile interfaces (#15854) <Thanks Anoop Johnson!>
■	Core: Add partition to TrackedFile (#16253) <Thanks Eduard Tudenhoefner!>
■	Core: Fix row ID assignment for EXISTING entry during a manifest merge (#16263) <Thanks Amogh Jahagirdar!>
■	Spark: Support writing shredded variant in Iceberg-Spark (#14297) <Thanks Aihua Xu and Neelesh Salian!>
■	Add TCK tests for Schema Evolution in BaseFormatModelTests [#15843] (Thanks GuoYu!)
○	Infra
■	Add Trivy CVE scan to CI [#15430] (Thanks Robin!)
■	Add PR title check workflow [#16101] (Thanks Manu!)
○	Python
■	Add Python 3.14 support to CI and build [#3299] (Thanks Adam & Kevin!)
■	Add `register_view` method to catalog for registering views [#3288] (Thanks Yuya!)
■	Add `load_view` support to REST catalog [#3224] (Thanks spr0els!)
■	Add initial pluggable file format writer API (`FileFormatWriter`, `FileFormatModel`, `FileFormatFactory`) [#3119] (Thanks Neelesh!)
■	Fix table config not updated during `Table.refresh()` for token/credential fields [#3327] (Thanks Yingjian!)
■	Add `overwrite` parameter to `catalog.register_table` [#3290] (Thanks Yuya!)
■	Fix DELETED manifest entry `snapshot_id` incorrectly set in `OverwriteFiles` [#3237] (Thanks Sotaro!)
■	Fix `ManifestEntry.snapshot_id` setter writing to wrong index, corrupting `status` field [#3257] (Thanks Sotaro!)
○	Rust
■	Add `EncryptionManager` with two-layer envelope encryption (KMS/KEK/DEK) [#2383] (Thanks Xander!)
■	Add `KeyManagementClient` trait and in-memory KMS implementation for encryption [#2339] (Thanks Xander!)
■	Add `StandardKeyMetadata` Avro-serialized key metadata for Iceberg encryption [#2340] (Thanks Xander!)
■	Add optional/required constructors for `MapType` in datatypes [#2405] (Thanks Liang!)
■	Add `read_with_metrics()` to `ArrowReader` exposing per-scan I/O byte metrics [#2349] (Thanks Matt & blackmwk!)
○	Go
■	Add maintenance CLI command wiring with stubs for all table operations [#1073] (Thanks Tanmay!)
■	Add commit retry with exponential backoff on OCC conflict errors [#912] (Thanks Andrei!)
■	Add OCC conflict validation framework with isolation levels and validators [#928] (Thanks Andrei!)
■	Add deletion vector reader for Iceberg v3 [#866] (Thanks Shreyas!)
■	Add clustered partitioned write path mirroring Java's ClusteredWriter [#948] (Thanks Tobias!)
○	C++
■	Add delete filter support for merge-on-read batches with position/equality deletes [#650] (Thanks Gang!)
■	Add streaming FileIO support with Arrow IO adapters for Avro/Parquet [#641] (Thanks Gang!)
■	Add separate `iceberg_data` library for data writers, deletes, and puffin [#631] (Thanks Junwang!)
■	Add ReachableFileCleanup strategy to expire snapshots [#592] (Thanks Xinli!)
■	Add retry with exponential backoff for failed transaction commits [#626] (Thanks SkylerLin!)
●	Releases
○	(kevin) 1.10.x and 1.11.x status 
■	1.11.x: RC1 with a few blockers addressed. Will have another RC.
○	Rust 0.9.1 is OUT! 
●	Discussion
○	Vladislav Sidorovich - Delta to Iceberg conversion review: https://github.com/apache/iceberg/pull/15407 
○	[Will / Kevin] Vortex integration
○	[Huaxin] Constraint support (proposal)
○	[Gabriel Igliozzi] Spark conf for session level time-travel proposal (issue)
○	PRs for review
■	VariantType to iceberg-rust: https://github.com/apache/iceberg-rust/pull/2423
■	DV read support to iceberg-rust: https://github.com/apache/iceberg-rust/pull/2414 
○	[Neelesh] Iceberg support for Spark 4.2
○	[Ryan] v4 spec changes
■	Relative paths
■	Columnar content stats
2026-04-22 (Recording)
●	Highlights
○	Java
■	Introduce foundational types for V4 manifest support #15049 (Thanks Anoop!)
■	Control merge schema evolution via table property in Spark 4.1 #15825 (Thanks Szehon!)
■	Add 404 response for REST catalog config endpoint when warehouse is missing #15746 (Thanks Oguzhan!)
■	Fix NPE in `ParquetAvroWriter` when schema contains variant type #15934 (Thanks Neelesh!)
■	Add runtime dependency guard for all bundled shadow JAR artifacts #15855 (Thanks Russell!)
■	Remove leaked transitive dependencies from Aliyun module runtime Jars #15858 (Thanks Ryan!)
■	Fix BigQuery dependency leak into runtime JARs #15655 (Thanks Alex!)
○	Python
■	Fix `ManifestEntry.snapshot_id` setter writing to wrong index, corrupting status field #3257 (Thanks Sotaro!)
■	Lock REST fixture to 1.10.1 to avoid Jetty upgrade breakage in CI #3240 (Thanks Fokko!)
■	Fix handling of optional/nullable `properties` in load namespace properties response #3169 (Thanks geruh!)
○	Rust
■	Fix incorrect Parquet INT96 timestamp values in ArrowReader #2301 (Thanks Matt!)
■	Add AGS1 streaming encryption/decryption support (AES-GCM, Java-compatible) #2286 (Thanks Xander!)
■	Fix NaN pushdown — `is_nan`/`not_nan` were returning constants instead of computing #2351 (Thanks Xander!)
■	Add `fixedbinary(n)` datum conversion support for `FixedSizedBinaryArray` #2348 (Thanks jeff-sqds!)
○	Go
■	Add support for row lineage in v3 tables #735 (Thanks Dao!)
■	Add conflict validation framework for concurrent commit detection #928 (Thanks Andrei!)
■	Retry `doCommit` on commit-conflict errors with exponential backoff #912 (Thanks Andrei!)
■	Add `RewriteDataFiles` for compaction execution with pos-delete cleanup #892 (Thanks Andrei!)
■	Add bin-pack compaction strategy with partition-aware planning #850 (Thanks Andrei!)
○	C++
■	Implement incremental changelog scan for table history diffing #611 (Thanks wzhuo!)
■	Add Puffin format constants, utilities, and JSON serialization for blob/file metadata #603 (Thanks ZhaoXuan!)
■	Support namespace separator in REST catalog #617 (Thanks Gang!)
■	Add `DeleteLoader` for position and equality delete files #610 (Thanks Gang!)
●	Releases
○	Java 1.10.2
■	Evaluating dependency changes
○	Java 1.11.0
■	https://github.com/apache/iceberg/milestone/59 
●	Discussion
○	<move discussion items from last meeting?>
○	[Anurag][DISCUSS] Future of Iceberg support in Apache DataFusion's Comet Spark Accelerator
■	https://github.com/apache/datafusion-comet/issues/2921 Comet community discussion
○	[Hongyue] Auto flushing the data files to manifests on SnapshotProducer to limit the memory ceiling in https://github.com/apache/iceberg/pull/15590
○	[Ryan] Extending Iceberg expressions (proposal)
○	
○	[Neelesh] Variant Community Update + Sync Proposal (dev thread: https://lists.apache.org/thread/f8l27lr55nlrdg4qwno29r796d4v2p8l) 
○	v4 relative path proposal
■	Base changes for v4 additions to the spec

2026-04-01 (Recording)
●	Highlights
○	Java
■	Spark 4.1: New Async Spark Micro Batch Planner (#15299) <Thanks Ruijing Li!>
■	API, Core: Add FileIO to Scan API (#15561) <Thanks Eduard Tudenhoefner!>
■	API, Core: Add overwrite-aware table registration (#15525) <Thanks Rishi!>
■	API, Core: Introduce foundational types for V4 manifest support (#15049) <Thanks Anoop Johnson!>
■	API, Core: Only include required stats fields (#15739) <Thanks Eduard Tudenhoefner!>
■	AWS: Add scheduled refresh for the S3FileIO held storage credentials (#15678) <Thanks Daniel Weeks!>
■	Core, Spark: Fix equality deletes non-deterministic schema ordering (#13873) <Thanks Russell Spitzer!>
■	Core: Add manifest partition pruning to DV validation in MergingSnapshotProducer (#15653) <Thanks Anoop Johnson!>
■	Core: Fix BinPackRewriteFilePlanner producing incorrect output file count with max-files-to-rewrite (#15576) <Thanks hemanthboyina!>
■	Core: Fix rewriting delete manifests in RewriteTablePathUtil (#15155) <Thanks wobu!>
■	Core: Fix useSnapshotSchema logic and projection in RESTTableScan (#15609) <Thanks Prashant Singh!>
■	Core: Load snapshot after it has been committed to prevent accidental cleanup of files (#15511) <Thanks Eduard Tudenhoefner!>
■	Core: Move Hadoop conf serialization into SerializableConfiguration (#15583) <Thanks Eduard Tudenhoefner!>
■	Core: Propagate Avro compression settings to manifest writers (#15652) <Thanks Russell Spitzer!>
■	Data, Spark, Flink: Add TCK for File Format API (#15441) <Thanks Joy Haldar!>
■	Flink: Add branch support to RewriteDataFiles maintenance task (#15672) <Thanks Maximilian Michels!>
■	Flink: Allow arbitrary post-commit maintenance tasks via IcebergSink Builder (#15566) <Thanks Maximilian Michels!>
■	Flink: Fix HashKeyGenerator SelectorKey cache ignoring writeParallelism and distributionMode (#15740) <Thanks Hayoung Lee!>
■	GCP: Add scheduled refresh for storage credentials held by GCSFileIO (#15696) <Thanks Eduard Tudenhoefner!>
■	GCS: Throw NotFoundException for nonexisting input GCS file (#15734) <Thanks Marius Grama!>
■	Kafka Connect: Fix CVE-2025-67721 in io.airlift:aircompressor by bumping to 2.0.3 (#15440) <Thanks Robin Moffatt!>
■	OpenAPI: Promote the S3 signing endpoint to the main spec (#15450) <Thanks Alexandre Dutra!>
■	Spark 4.1: Fix async microbatch plan bugs (#15670) <Thanks Ruijing Li!>
■	Spark 4.1: Set data file sort_order_id in manifest for writes from Spark (#15150) <Thanks jbewing!>
■	Spark: Validate Z-order rewrite does not conflict with internal ICEZVALUE column name (#15706) <Thanks Yaniv Zalach!>
■	Spark: fix NPE thrown for MAP/LIST columns on DELETE, UPDATE, and MERGE operations (#15726) <Thanks antonlin1!>
○	Python
■	Add type mapping tables between PyIceberg and PyArrow in docs [#3098] (Thanks committobetter & Kevin!)
■	Fix nanosecond timestamp conversion silently dropping non-UTC timezone [#3142] (Thanks Neelesh!)
■	Fix Glue `create_table` for S3 Tables federated databases [#3058] (Thanks James!)
■	Fix handle empty HEAD response when body is missing or null [#3041] (Thanks Antonio & Kevin!)
○	Rust
■	Honor compression settings for `metadata.json` on write [#1876] (Thanks emkornfield & Kevin!)
■	Add catalog test suite to unify catalog behavior [#2131] (Thanks blackmwk!)
■	Add DataFusion Comet to Users section of README [#2283] (Thanks Matt!)
■	Add AES-GCM crypto primitives for Iceberg encryption support [#2026] (Thanks Xander!)
■	Fix `-1` snapshot ID sentinel usage and add deserialization test [#2294] (Thanks Geser!)
○	Go
■	Add equality delete writing support for partitioned tables [#823] (Thanks Andrei!)
■	Add write-default and initial-default value support during Arrow schema projection (v3) [#779] (Thanks PranjalChaitanya!)
■	Add Parquet support for nanosecond timestamp types (v3) [#819] (Thanks Andrei!)
■	Add refresh for vended credentials dynamically from load table response [#795] (Thanks Tyler!)
○	C++
■	Add incremental scan API for table scanning [#559] (Thanks wzhuo!)
■	Add roaring-based position bitmap for efficient delete position tracking [#595] (Thanks Gang & emkornfield!)
■	Add initial OAuth2 authentication with static token and client credentials flows to REST catalog [#577] (Thanks lishuxu!)
■	Implement `IncrementalAppendScan` for scanning incremental table appends [#590] (Thanks wzhuo!)
■	Add foundational Puffin file format data structures and constants [#588] (Thanks ZhaoXuan!)
●	Releases
○	[Kevin] 0.9.1 Rust patch release (devlist)
○	[Amogh] 1.10.x patch release milestone
○	[Aihua] 1.11.0 Java release check milestones
■	Removing GCP dependencies from runtime Jars (#15655)
■	Need fixes on top of LICENSE/NOTICE changes (#15449)
■	Expose HostnameVerificationPolicy in TLSConfigurer (#15500)
●	Agenda Items
○	Iceberg Summit (next week!)
○	[Alex] Collation Support - Bumped from last meeting
○	[Alex/Talat] - GCP Dependencies PR
○	[Anurag][DISCUSS] Future of Iceberg support in Apache DataFusion's Comet Spark Accelerator
■	https://github.com/apache/datafusion-comet/issues/2921 Comet community discussion
○	
○	[Hongyue] Auto flushing the data files to manifests on SnapshotProducer to limit the memory ceiling in https://github.com/apache/iceberg/pull/15590
○	[Huaxin] Vote: REST catalog list/load function endpoints (https://github.com/apache/iceberg/pull/15180) — please review and vote on the dev list
○	[Stevel]: Bad news from variant query benchmarks

2026-03-11 (Recording)
●	Highlights
○	Infra:
■	Add CodeQL workflow for GitHub Actions security scanning #3060 (Thanks Kevin!)
■	Add explicit least-privilege permissions to all GitHub Actions workflows #3082 (Thanks Kevin!)
■	Set GitHub Actions `max-parallel` to 15 per Apache infra guidance #3057 (Thanks Kevin!)
■	Use `ubuntu-slim` runner for lightweight CI jobs to save infra resources #3107 (Thanks Junwang!)
○	Java/Docs:
■	API, CORE, Flink, Spark: Deprecate Snapshot.changes Methods with SnapshotChange Utility (#15241) <Thanks Russell Spitzer!>
■	API, Core: Align offsets of field stats with Design doc / Spec (#15432) <Thanks Eduard Tudenhoefner!>
■	Core, Spark: add the comment table property key (#15531) <Thanks Steven Zhen Wu!>
■	Core, Spark: Adds a Table Property for Relying on Identifier Fields (#15372) <Thanks Russell Spitzer!>
■	Core, Spark: Rename read.identifier-fields.rely to identifier-fields.rely (#15495) <Thanks Russell Spitzer!>
■	Core, Spark: Unify bulk deletion (#15501) <Thanks Eduard Tudenhoefner!>
■	Core: Add properties to InMemoryFileIO (#15469) <Thanks Eduard Tudenhoefner!>
■	Core: Add test for freshness-aware table loading with lazy snapshot loading (#15274) <Thanks gaborkaszab!>
■	Core: Avoid exceptions for accessing schema for metadata tables in SnapshotUtil (#15387) <Thanks Anton Okolnychyi!>
■	Core: Detect and merge duplicate DVs for a data file and merge them before committing (#15006) <Thanks Amogh Jahagirdar!>
■	Core: Make sequence number conflicts retryable when there are concurrent commits (#15126) <Thanks Xinyi Lu!>
■	Core: populate manifest created/replaced/kept count when commit a snapshot (#15003) <Thanks Hongyue/Steve Zhang!>
■	Core: Rename tableIo to tableIO (#15582) <Thanks Eduard Tudenhoefner!>
■	Core: Support parallel execution when scanning entries in ManifestGroup (#15426) <Thanks Hongyue/Steve Zhang!>
■	Core: Track & close FileIO used for remote scan planning (#15439) <Thanks Eduard Tudenhoefner!>
■	Docker, Docs, Site: Add Flink quickstart (#15062) <Thanks Robin Moffatt!>
■	Docs: Add blog post about File Format API (#15380) <Thanks pvary!>
■	docs: Add CREATE DATABASE step before CREATE TABLE in Spark quickstart (#15513) <Thanks Ramesh Reddy Adutla!>
■	Docs: Add informational properties section for table comment (#15367) <Thanks yguy-ryft!>
■	docs: udf spec, add newline to properly render lists (#15516) <Thanks Kevin Liu!>
■	Flink: Add the possibility to use Coordinator Lock when using Flink SQL (#15459) <Thanks GuoYu!>
■	Flink: Backport Add the possibility to use Coordinator Lock when using Flink SQL to 2.0 and 1.20 (#15562) <Thanks GuoYu!>
■	Flink: Backport SQL support for dynamic iceberg sink (#15444) <Thanks Swapna Marru!>
■	Flink: Backport TableMaintenance Support Coordinator Lock to 1.20 and 2.0 (#15438) <Thanks GuoYu!>
■	Flink: SQL support for dynamic iceberg sink (#15279) <Thanks Swapna Marru!>
■	Flink: Support Variant to Flink 2.1 (#15265) <Thanks GuoYu!>
■	Flink: TableMaintenance Support Coordinator Lock (#15151) <Thanks GuoYu!>
■	JDBC: JDBC Catalog should handle Postgres exception for duplicate keys (#15434) <Thanks Han You!>
■	OpenAPI: Add SetPartitionStatisticsUpdate/RemovePartitionStatisticsUpdate to TableUpdate (#14957) <Thanks feefs!>
■	OpenAPI: Include storage credentials for PlanTableScanResponse/FetchPlanningResultResponse on plan completed given include-credentials flag is set (#15524) <Thanks Eduard Tudenhoefner!>
■	Revert "Move deleted files to Hadoop trash if configured (#14501)" (#15386) <Thanks Daniel Weeks!>
■	Spark 3.4, 3.5, 4.0, 4.1: Don't Use table FileIO for Spark Checkpoints (#15574, #15239) <Thanks c2zwdjnlcg!>
■	Spark 4.0/4.1: Display write metrics on SQL UI (#15104) <Thanks Manu Zhang!>
■	Spark 4.1: Introduce modes in SparkWriteBuilder (#15374) <Thanks Anton Okolnychyi!>
■	Spark 4.1: Migrate to new version framework in DSv2 (#15240) <Thanks Anton Okolnychyi!>
■	Spark 4.1: Refactor metadata column references to use asRef() method (#15376) <Thanks Anton Okolnychyi!>
■	Spark 4.1: Rename expectedSchema to projection for clarity (#15366) <Thanks Anton Okolnychyi!>
■	Spark 4.1: Simplify time travel option extraction in IcebergSource (#15375) <Thanks Anton Okolnychyi!>
■	Spark, Arrow, Parquet: Add vectorized parquet read support for `DELTA_LENGTH_BYTE_ARRAY` & `DELTA_BYTE_ARRAY` encodings (#15362) <Thanks jbewing!>
■	Spark, Arrow, Parquet: Add vectorized read support for parquet BYTE_STREAM_SPLIT encoding (#15373) <Thanks jbewing!>
■	Spark: Add ExecutorService support to RewriteTablePath (#15381) <Thanks Maximilian Michels!>
■	Spark: Add sort_by parameter to rewrite_manifests procedure (#15467) <Thanks hemanthboyina!>
■	Spark: Backport: Add ExecutorService support to RewriteTablePath (#15578) <Thanks Maximilian Michels!>
■	Spark: Fix javadoc mentioning Spark 3.3 in Spark 3.4 benchmark classes (#15544) <Thanks Anshul Baliga!>
■	Build: Bump roaringbitmap from 1.3.0 to 1.6.0 #14991
○	Python
■	Accept all valid HTTP methods in IRC's `ConfigResponse` for Polaris compatibility #3010 (Thanks Sumanth & geruh!)
■	Fix handle empty HEAD response to avoid pydantic parse error #3041 (Thanks Antonio!)
■	Support `storage-credentials` field in REST catalog `LoadTableResult` for vended credentials #3042 (Thanks rcjverhoef!)
■	Add ViewMetadata read support and `create_view` to REST Catalog #2154 (Thanks Alex!)
■	Add concurrency safety validation checks using `DeleteFileIndex` #3049 (Thanks Gabriel!)
■	Optimize manifest pruning in snapshot overwrite operations for performance #3011 (Thanks Gabriel!)
■	Surface `TooManyRequestsError` exception for HTTP 429 responses #3048 (Thanks Marcin!)
○	Rust
■	Integrate Storage trait with FileIO, replacing OpenDalStorage directly #2116 (Thanks Shawn!)
■	Add compression support for `metadata.json` writes via `write.metadata.compression-codec` #1876 (Thanks emkornfield!)
■	Add `isnan` predicate pushdown support from DataFusion to Iceberg #2142 (Thanks Kaiqi!)
■	Add timestamp type support in `create_column` for schema evolution #2180 (Thanks Dylan!)
■	Add Parquet metadata size hint option to `ArrowReaderBuilder` #2173 (Thanks Matt!)
■	Pass data/delete file sizes to reader to eliminate redundant `stat()` calls #2175 (Thanks Matt!)
■	Implement `AsyncFileReader::get_byte_ranges` with range coalescing for efficient reads #2181 (Thanks Matt!)
■	Avoid redundant `create_parquet_record_batch_stream_builder()` call for migrated tables #2176 (Thanks Matt!)
○	Go
■	Add support for merge-on-read deletes using position delete files #721 (Thanks Alex!)
■	Add functions for adding and replacing data directly with data files #723 (Thanks Adam!)
■	Add Puffin reader and writer (uncompressed) #676 (Thanks Shreyas!)
■	Add support for staged table creation in REST catalog #754 (Thanks Lovro!)
■	Add `RegisterView` to REST catalog for view migration support #753 (Thanks Shubhendu!)
■	Add registry pattern for IO schemes, moving cloud storage to `io/gocloud` #709 (Thanks Alessandro!)
■	Roll parquet files based on actual compressed size, matching Java/Rust behavior #759 (Thanks Tobias!)
○	C++
■	Implement DataWriter for writing Iceberg data files with Parquet/Avro support #552 (Thanks Xinli!)
■	Add SnapshotManager with test cases derived from Java implementation #542 (Thanks Junwang!)
■	Implement BasicAuthManager to support basic authentication in REST catalog #564 (Thanks lishuxu!)
■	Add JSON serde for expressions to support predicate pushdown #553 (Thanks Innocent!)
●	Releases
○	Rust 0.9.0 RC1 is out! (devlist)
○	Go 0.5.0 release is out! (devlist)
○	PyIceberg 0.11.1 is out! (devlist)
○	[Amogh] 1.10.x patch release
○	[Aihua] 1.11.0 Java release check milestones 
■	Iceberg 1.11.0 Release Track 3 of 6 blockers remaining
■	Potentially: https://github.com/apache/iceberg/pull/15500#issuecomment-4033352180
●	Agenda Items
○	[Russ] Iceberg Summit - Hotel Block Rate Ends March 16th!
○	[Kevin] Publishing Flink|Spark Iceberg Docker image
■	License questions (what are the requirements for Docker image?)
■	Distribution can be problematic
○	[Kevin] Replace Minio for quick start #15577
○	
○	[Alex] Collation Support
○	[Kevin] Agent automated PRs 
○	[Prashant] Run Github CI workflows in fork resources than the main resources like apache spark does https://github.com/apache/spark/pull/32092 to protect against Agents bombarding our CIs 


2026-02-18 (Recording)
●	Highlights
○	Spec
■	Introduce SQL UDF specification (#14117) <Thanks Yufei Gu!>
■	Add AccessDelegation header to planAPI calls (#14781) <Thanks Prashant Singh!>
■	Add referenced-by in loadTable API #13810  <Thanks Prashant Singh!>
■	REST Spec: Include SetPartitionStatisticsUpdate and RemovePartitionStatisticsUpdate in TableUpdate union (#15115) <Thanks Logesh R!>
■	REST: add support for data access parameter to registerTable (#15231) <Thanks Alexandre Dutra!>
○	Site: 
■	add docs about Requesting Slack Integrations (#15170) <Thanks Kevin Liu!>
■	Document v3 types (#14888) <Thanks Innocent Djiofack!>
■	Add RSS feed for blogs (#15071) <Thanks Manu Zhang!>
○	Docs:
■	Add C++ library to implementation status (#15107) <Thanks Feiyang Li!>
■	blog post for C++ 0.2.0 release (#15141) <Thanks Gang Wu!>
■	blog post for iceberg-python 0.11.0 release (#15290) <Thanks geruh!>
■	blog post for iceberg-rust 0.8.0 release (#15221) <Thanks Kevin Liu!>
■	Add guidelines for AI-generated contributions (#15213) (Thanks Junwang!)
○	Java
■	API: Implement properties method in EncryptingFileIO (#15289) <Thanks Yuya Ebihara!>
■	API: Optimize NOT IN and != predicates for single-value partition manifests (#15064) <Thanks Joy Haldar!>
■	API: Use Transform#isIdentity in PartitionSpec#identitySourceIds (#15066) <Thanks Raunaq Morarka!>
■	AWS: Prefer custom credential provider if specified (#15249) <Thanks Bryan Keller!>
■	Core, Data: File Format API interfaces (#12774) <Thanks pvary!>
■	Core, Spark: Moving Spark to use the new FormatModel API (#15328) <Thanks pvary!> ()
■	Core, REST: Add support for overwrite in RegisterTableRequest (#15248) <Thanks Alexandre Dutra!>
■	Core, Spark 4.1: Fix distributed planning for CoW operations (#15246) <Thanks Anton Okolnychyi!>
■	Core, Spark 4.1: Fix querying equality deletes with schema evolution (#15268) <Thanks Anton Okolnychyi!>
■	Core, Spark: Rename RequiresRemoteScanPlanning to SupportsDistributedScanPlanning (#15184) <Thanks Eduard Tudenhoefner!>
■	Core: Avro: Row Lineage Column (ROW_ID) is not populated correctly in case the Data File doesn't have them (#15187) <Thanks Ayush Saxena!>
■	Core: Convert metrics to Content Stats (#15251) <Thanks Eduard Tudenhoefner!>
■	Core: Do not cleanup when CREATE transactions fail with 503 (#15051) <Thanks Alessandro Nori!>
■	Core: Fix compute_table_stats failures with concurrent writes (#15148) <Thanks hemanthboyina!>
■	Core: Fix data loss in partial variant shredding (#15087) <Thanks yan zhang!>
■	Core: Fix metadata table scans with useRef by preserving metadata schema (#15276) <Thanks Rui Li!>
■	Core: Freshness-aware table loading in REST catalog (#14398) <Thanks gaborkaszab!>
■	Core: Implement register view for REST catalog (#14870) <Thanks Ajantha Bhat!>
■	Core: Include query params into ETag calculation in reference IRC (#15057) <Thanks gaborkaszab!>
■	Core: Invalidate ShreddedObject serialization cache on remove (#15097) <Thanks Huaxin Gao!>
■	Core: Prevent exceptions in ExpressionUtil for unpartitioned tables (#15243) <Thanks Anton Okolnychyi!>
■	Core: Remove deprecation from ViewProperties.WRITE_METADATA_LOCATION (#15250) <Thanks gaborkaszab!>
■	Core: Skip unnecessary metadata refresh when producing snapshot event after merge append (#14709) <Thanks gaborkaszab!>
■	Fix Internal to Generic conversion of TIMESTAMP_NANO (#15099) <Thanks Ayush Saxena!>
■	Fix incorrect partition bounds calculation in manifest on deletion (#15127) <Thanks Dong Wang!>
■	Spark 4.1 | 4.0 | 3.5 | 3.4: Fail publish_changes procedure if there's more than one matching snapshot (#14955) <Thanks Sam Wheating!>
■	Spark 4.1: Add Merge WriteSummary to Snapshot Summary (#15014) <Thanks Szehon Ho!>
■	Add Flink Quickstart docker image #15124 (Thanks Robin!)
○	Python
■	Add support for building aarch64 wheels on Linux #2973 and mac Intel wheels #2976 (Thanks Geruh and Alex!)
■	Fix manifest cache O(N²) inefficiency by caching individual ManifestFile objects #2951 (Thanks Kevin!)
■	Add tell() method to OutputStream writers to track written bytes #2998 (Thanks geruh!)
■	Add Geometry and Geography primitive types for Iceberg v3 #2859 (Thanks Sam!)
■	Add namespace_exists method to all catalog implementations #2972 (Thanks Alex!)
■	Add Entra ID auth manager using DefaultAzureCredential #2974 (Thanks Kevin!)
■	Allow reading PyArrow timestamptz columns as Iceberg timestamp type #2708 (Thanks Kevin!)
■	Add anon property to fsspec ADLS file IO config for DefaultCredential support #2661 (Thanks NikitaMatskevich!)
■	Fix test isolation by ignoring local PyIceberg config during tests #3006 (Thanks geruh!)
○	Rust
■	Improve integration tests setup for CI and dev env #2071, #2074, #2076, #2078, #2085, #2090, #2091 (Thanks Renjie and Kevin!)
■	Implement Storage trait #2080, in-memory FileIO #2097, local FileIO #2094, storage configs #2072 (Thanks Shawn!)
■	Add DataFusion integration predicate pushdown support; for boolean #2082 and timestamp scalar #2069 (Thanks Liang-Chi!)
■	Fix Python binding upper version bound to allow Python 3.13+ #2110 (Thanks geruh!)
■	Replace rust_decimal with fastnum for full 38-digit decimal precision #2063 (Thanks Nathan!)
■	Fix REST catalog filtering sensitive headers (Authorization, Cookie) from error logs #2130 (Thanks Cole!)
■	Fix S3 Tables warehouse interpreted as table location instead of metadata location #2115 (Thanks emkornfield!)
■	Factor out CompressionCodec to common location and add Gzip support #2081 (Thanks emkornfield!)
○	Go
■	Add table overwrite functionality #674 (Thanks Arun & Matt!)
■	Add initial Hive Catalog support #678 (Thanks Kanthi!)
■	Add copy-on-write delete support for tables #718 (Thanks Alex!)
■	fix(table): use proper data file names #702 (Thanks Matt!)
■	fix: explicitly pass purgeRequested=false in DropTable #707 (Thanks Shubhendu!)
○	C++
■	Implement set snapshot #509, update table stats #511, update partition stats #538  (Thanks Feiyang!)
■	feat: add compression config to writer properties #524 (Thanks Gang!)
■	Implement NoopAuthManager and integrate it with RestCatalog (#544) (Thanks lishuxu!)
■	Refactor manifest writer API by removing MakeVxWriter in favor of MakeWriter (#551) (Thanks Junwang!)
■	Add JSON serde support for expression operations (#532) (Thanks Innocent!)
●	Releases
○	C++ 0.2.0 release (blog)
○	Rust 0.8.0 release (blog)
○	Python 0.11.0 release (blog)
○	[Aihua] 1.11.0 Java release check milestones
■	[Peter] File Format API is merged. Thanks everyone!
●	Agenda items
○	[Steven] Need more reviews on the geospatial predicate and bounding box literal PR
○	[Vishal] Could we merge changes related to the UUID comparator bugfix if there are no more comments? Metrics evaluation is now more lenient and allows reading manifest entries prepared with the signed comparator (devlist thread, issue, PR)
○	[Amogh] Implications of adding jitpack as a repository (added so that roaringbitmap could be upgraded to the latest version, for newer spark version support)
○	[Yingjian] Branch schema evolution 
○	[Peter] Secondary Indexes discussion started:
■	https://docs.google.com/document/d/1N6a2IOzC6Qsqv7NBqHKesees4N6WF49YUSIX2FrF7S0
■	https://docs.google.com/document/d/1x-0KT43aTrt8u6EV7EgSietIFQSkGsocqwnBTHPebRU
○	[talat] Iceberg Delta Encoded Schemas https://s.apache.org/iceberg-delta-schemas
○	[Kevin] Publishing Flink|Spark Iceberg Docker image
2026-01-28 (Recording)
●	Highlights
○	Site
■	Add Iceberg Summit 2026 section to homepage #14988 (Thanks Russell!)
■	Iceberg Project Blog! https://iceberg.apache.org/blog/
●	Announcing Iceberg Summit 2026 #15013 (Thanks Kevin & Danica!)
●	Apache Iceberg C++ 0.2.0 Release #15141 (Thanks Gang!)
●	(WIP) Apache Iceberg Rust 0.8.0 Release
■	Site: Add RSS feed for blogs #15071 (Thanks Manu!)
■	Add C++ library to implementation status #15107 (Thanks Feiyang!)
○	Java
■	Core: Implement register view for REST catalog #14870 (Thanks Ajantha!)
■	Core: Unlink table metadata's last-updated timestamp from snapshot timestamp #14504 (Thanks Steve!) 
■	Core: Freshness-aware table loading in REST catalog #14398 (Thanks Gabor!)
■	Core: Reduce manifest logging noise on drop table #14969 (Thanks Steve!)
■	Core, Hive: Detect if a view already exists when registering a table #15010 (Thanks Eduard!)
■	Add idempotency adapter and E2E coverage #14773 (Thanks Huaxin!)
■	REST Spec: clarify uniqueness of ETags for table metadata responses #15045 (Thanks Daniel!)
■	Include key metadata in manifest tables (Spark 4.1) #15041 (Thanks Thomas!)
■	Make StandardEncryptionManager serializable #14751 (Thanks Thomas!)
■	Spark 4.1: Add Merge WriteSummary to Snapshot Summary #15014 (Thanks Szehon!)
■	Spark 4.1: Initial support for MERGE INTO schema evolution #14970 (Thanks Szehon!)
■	BigQuery: Eliminate redundant table load by using ETag for conflict detection #14940 (Thanks Joy!)
■	Flink: Dynamic Sink: Add case-insensitive field matching #14729 (Thanks Maximilian!)
■	Kafka Connect: fix table UUID check #15011 (Thanks Bryan!)
■	Upgrade to Spark 3.5.8 #15033 (Thanks Manu!)
■	Bump to Parquet 1.17.0 #14924 (Thanks Fokko!)
■	Core: Drop support for Java 11 #14400 (Thanks Manu!)
○	PyIceberg
■	Add Set Current Snapshot to ManageSnapshots API #2871 (Thanks Drew & Chinmay!)
■	Consolidating InMemoryCatalog and SqlCatalog tests #2906 (Thanks Neelesh!)
■	Add support for rolling back to snapshot #2878 (Thanks Drew!)
■	Fix handle empty body in AWS SigV4 signing #2827 (Thanks Jiajia!)
■	Add check table UUID to detect table replacement #2890 (Thanks Drew!) 
■	Add support for rest scan planning #2864 (Thanks Drew!)
■	Fix auth manager S3 signer bug #2846 (Thanks Soham!)
■	Add make notebook #2528 (Thanks Kevin!)
■	Make REST catalog namespace separator configurable #2826 (Thanks Alex!)
■	Add support for rolling back to timestamp #2879 (Thanks Drew!)
■	Fix: preserve HMS table properties during commits #2927 (Thanks Bharath!)
■	Add DeleteFileIndex to improve position delete lookup #2918 (Thanks Drew!)
■	Fix: Cast smaller integer types to int32/int64 on write for Spark compatibility #2799 (Thanks Somasundaram!)
■	Fix: Allow update_column to change required for list elements and map values #2798 (Thanks Somasundaram!)
■	Add AWS profile support to glue and fsspec s3 fileio #2948 (Thanks Stats!)
■	Block schema field drop if it is referenced by an active partition or sort field #2410 (Thanks Gabriel!)
○	Iceberg-Rust
■	Datafusion integrations: 
●	LIMIT pushdown #2006 (Thanks Liang-Chi!)
●	Schema validation for partition projection #2008 (Thanks Liang-Chi!)
●	Support CREATE TABLE #1972 (Thanks Shawn!)
●	Add support for DROP TABLE #2033 (Thanks Shawn!)
●	Add LIKE predicate pushdown for StartsWith patterns #2014 (Thanks Liang-Chi!)
■	rfc: Making Storage a Trait #1885 (Thanks Shawn!)
■	allow v2 to v3 table upgrades with existing snapshots #2010 (Thanks Aditya!)
■	Add Storage, StorageFactory, StorageConfig #2061 (Thanks Shawn!)
■	Simplify test setup by starting container only once #2071 (Thanks Renjie!)
■	Cleanup integration tests #2074 (Thanks Renjie!)
○	Iceberg-cpp
■	Implement location provider #467 (Thanks wzhuo!)
■	add snapshot update #408 (Thanks Junwang!)
■	implement reference visitor #491 (Thanks Gang!)
■	support expire snapshots #490 (Thanks dongxiao!)
■	implement update column #498 (Thanks Guotao!)
■	implement update location #508 (Thanks Feiyang!)
■	add restcatalog authentication api #479 (Thanks lishuxu!)
■	add FastAppend #516 (Thanks Junwang!)
○	Iceberg-go
■	Close writers on error #667, #666, #670, #683, #685, #687, #688 (Thanks ferhat & Matt!)
■	Send custom header to IRC #652 (Thanks Alex!)
■	Improve ExpireSnapshots #677, #671, #679, #672 (Thanks Krutika!)
■	add pagination support to ListNamespaces #694 (Thanks Sumisha!)
■	Add AuthManager support #579 (Thanks Alex!)
●	Releases
○	Iceberg-Rust 0.8.0 is out!
○	Iceberg-Cpp 0.2.0 is out!
○	Last few remaining items on PyIceberg 0.11.0 release
●	Agenda Items
○	1.11.0 milestones (Aihua is RM)
■	Targeting release ~Feb
■	File Format API
■	Spark 4.1 functionalities
●	Implement version changes
■	Remote scan planning
■	Amogh’s DV fix #15006
■	Spark 3.4 is ~deprecated~
○	automate checking java dependency changes #14885
○	Slack Plugins (devlist thread)
■	Add to https://iceberg.apache.org/community/#slack about Plugin
○	Iceberg Summit Updates (https://www.icebergsummit.org/)
■	Over 400 Submissions
■	Selection Committee to finish review this week
■	Registration is open (Early Bird until Feb 15th)
○	Proposal: Efficient Column Updates in Iceberg (Anurag will join at 9:30 AM PST)
○	Iceberg-Terraform updates
■	PRs out for initial versions of Namespace, Table resource
○	Deprecate partition summary from snapshot summary info since we now have Partition stats

2026-01-07 (Recording)
●	Highlights
○	Iceberg Summit 2026 CFP open until Jan 18!
○	Java
■	API, Core: Scan API for partition stats (#14640) <gaborkaszab>
■	API, Spark: Optimize NOT IN and != predicate evaluation for fields containing a single-value (#14593) <Joy Haldar>
■	Core: Close planFiles() iterable in CatalogHandler (#14891) <Eduard Tudenhoefner>
■	Core: Simplify handling of the current planId in client side of remote planning (#14883) <Eduard Tudenhoefner>
■	OpenAPI: Etag for CommitTableResponse (#14760) <Christian>
■	Spark: Backport: Add Spark app name to env context for Spark v3.4, 3.5, 4.0 (#14981) <Varun Lakhyani>
■	Spark: Add ordering to TestSelect to remove flakiness (#14956) <Huaxin Gao>
■	Spark: Initial support for 4.1.0 <manuzhang>
■	Spark: Enable remote scan planning with REST catalog (#14822) <Eduard Tudenhoefner>
■	Spark: Order results to fix test flakiness with remote scan planning (#14894) <Eduard Tudenhoefner>
■	Spark 3.4 | 3.5: Enable remote scan planning (#14963) <Prashant Singh>
■	Spark: Add Spark app name to env context (#14976) <Stas Pak>
■	Flink: Fix equalityFieldColumns always null in IcebergSink (#14952) <GuoYu>
■	Flink: DynamicSink: Report writer records/bytes send metrics (#14878) <aiborodin>
■	Flink: Dynamic Sink: Fix serialization issues with schemas larger than 2^16 bytes (#14880) <Maximilian Michels>
■	Site: Updates for 1.10.1 Release (#14907) <Huaxin Gao>
■	AWS: Merge catalog properties with properties prefixed with client.credentials-provider. (#14608) <Thomas Powell>
■	GCP: Add service account impersonation support for BigQueryMetastoreCatalog (#14447) <Joy Haldar>
■	Hive: Update view query in HMS when replacing view (#14831) <wuya>
○	PyIceberg
■	Official Python 3.13 support, thanks Kevin!
■	Support for getting the supported endpoints from the REST catalog, thanks Drew!
■	Foundational work for scan planning client support, thanks again Drew!
○	Iceberg-Rust
■	Thanks Alan for fixing IEEE 754 ordering for float and double
■	Thanks Shawn for adding logic to convert an Arrow schema to an Iceberg schema (with IDs 🎉)
■	Thanks Kevin for fixing the release script
■	Thanks Lo for preventing a potential deadlock during scan-planning
■	Thanks Matt for fixing the Decimal.
○	Iceberg-cpp
■	Thanks Gang for implementing the transaction api and delete file index
■	Thanks Heartlinked for adding REST catalog functionalities (create, stage-create, list and update, load and drop)
■	Thanks Junwang for adding rolling manifest writer and snapshot cached manifests
■	Thanks Xinli for adding FileWriter interface for data file writers
○	Iceberg-go
■	Thanks Dao for adding support for V3 Unknown Type
■	Thanks Tobias for adding support for row lineage tracking in metadata update 
■	Thanks ferhat for fixing potential leaks in rest response bodies
●	Releases
○	Iceberg-Rust 0.8.0 is ready for a second round of voting
○	Iceberg 1.11.0 [DISCUSS] thread is out
○	PyIceberg 0.11.0 is being wrapped up
●	Agenda items
○	[Steven] should the spec calls out certain invalid writer behaviors in the implementation notes section.
■	Disallow row undeletion by unsetting the bit in updated DV or position delete (dev thread, spec PR)
■	Add implementation notes for writer behavior to avoid duplicate files (dev thread)
■	Writers shouldn’t add back files that are already deleted, which can lead to race conditions like following
●	T1: add F1 in S1
●	T2: delete F1 and add F2 in S2
●	T3: add F3 in S3
●	T4: expire snapshot S1 and S2 and schedule F1 for deletion. Concurrently, another DML adds back F1. This could cause the table in broken state with missing data file F1.
○	[Vishal] Could fixing the non-RFC compliant UUID comparison bug be targeted for Iceberg 2.0.0 as it introduces breaking changes? (devlist thread, issue, PR)
○	[Ajantha] Should the “register view” update the catalog name? (spark compatibility issue) https://lists.apache.org/thread/yt430r50xp9v5jmhf79m3o56q05x9k3v
○	[Kevin] Deprecate Spark 3.4
○	[Kevin] project blog, iceberg.apache.org/blogs/

<Moved the rest of the syncs to a new tab>
