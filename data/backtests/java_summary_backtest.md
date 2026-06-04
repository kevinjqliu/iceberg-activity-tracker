# Java Summary Backtest

- Sections evaluated: `2`
- Note PRs: `23`
- Found in sync windows: `23`
- Hits@10: `10/23`
- Hits@20: `16/23`

## 2026-05-13 Java

- Previous sync date: `2026-04-22`
- Candidate commits: `132`
- LanceDB prior examples: `141`
- Note PRs: `7`
- Found in sync window: `7`
- Hits@10: `3/7`
- Hits@20: `5/7`
- Median found rank: `17.0`

### Found Note PRs

- rank `1` score `102` (heur `92`, lancedb `10`) #14297: Spark: Support writing shredded variant in Iceberg-Spark (#14297)
- rank `2` score `100` (heur `89`, lancedb `11`) #15854: Core: Add implementations of v4 TrackedFile interfaces (#15854)
- rank `7` score `92` (heur `83`, lancedb `9`) #16092: Core: Add builders for v4 structs (#16092)
- rank `17` score `70` (heur `56`, lancedb `14`) #16253: Core: Add partition to TrackedFile (#16253)
- rank `18` score `70` (heur `62`, lancedb `8`) #16263: Core: Fix row ID assignment for EXISTING entry during a manifest merge (#16263)
- rank `71` score `41` (heur `38`, lancedb `3`) #15843: Data: Add TCK tests for Schema Evolution  in BaseFormatModelTests (#15843)
- rank `126` score `0` (heur `-3`, lancedb `3`) #16163: Open API: Remove runtime Jar from build and deploy (#16163)

### False Positives In Top 10

- score `99` #12892: Core, Catalogs: Add support for unique table locations via catalog property (#12892)
- score `95` #16245: Spark: backport PR #15512 to v3.4, v3.5, v4.0 for WAP branch delete fix (#16245)
- score `95` #16215: Spark: Fix LICENSE/NOTICE compliance for all versions of spark-runtime (v3.4, v3.5, v4.0, v4.1) (#16215)
- score `94` #16241: Spark: Backport support writing shredded variant in Iceberg-Spark (#16241)
- score `83` #15475: Flink: Add Nanosecond Precision Support for Flink-Iceberg Integration (#15475)
- score `78` #16049: Flink: Fix JdbcLockFactory to allow ClientPoolImpl connection retry (#16049)
- score `77` #16240: Flink: Backport add Nanosecond Precision Support for Flink-Iceberg Integration to Flink 1.20 (#16240)

## 2026-06-03 Java

- Previous sync date: `2026-05-13`
- Candidate commits: `116`
- LanceDB prior examples: `149`
- Note PRs: `16`
- Found in sync window: `16`
- Hits@10: `7/16`
- Hits@20: `11/16`
- Median found rank: `14.5`

### Found Note PRs

- rank `1` score `104` (heur `93`, lancedb `11`) #15634: Core, Parquet: Allow for Writing Parquet/Avro Manifests in V4 (#15634)
- rank `2` score `102` (heur `89`, lancedb `13`) #15596: Flink: Support writing shredded variant (#15596)
- rank `3` score `97` (heur `81`, lancedb `16`) #16569: API, Core, Orc: Implement project() for partition statistics scan API (#16569)
- rank `5` score `89` (heur `76`, lancedb `13`) #16174: Core: Add V4 location relativization utilities (#16174)
- rank `7` score `82` (heur `72`, lancedb `10`) #16144: OpenAPI: Add CatalogObjectIdentifier schema (#16144)
- rank `8` score `79` (heur `72`, lancedb `7`) #14234: Spec: Add v4 content stats representation (#14234)
- rank `9` score `74` (heur `67`, lancedb `7`) #16572: Core: v4 table metadata location should be optional (#16572)
- rank `13` score `69` (heur `60`, lancedb `9`) #15630: [SPEC] Add relative paths to v4 spec (#15630)
- rank `16` score `68` (heur `56`, lancedb `12`) #16534: Spark: Backport Add _row_id and _last_updated_sequence_number raeder in Orc to support lineage (#16534)
- rank `17` score `68` (heur `60`, lancedb `8`) #16097: Flink: Support UUID type in Avro and Parquet readers and writers (#16097)
- rank `19` score `61` (heur `55`, lancedb `6`) #16400: REST Spec: Add unregister table endpoint (#16400)
- rank `32` score `51` (heur `44`, lancedb `7`) #14998: Core, Orc: Remove deprecated partition stats read functionality (#14998)
- rank `41` score `46` (heur `38`, lancedb `8`) #16328: Spark: Also disable min/max aggregation push down for binary (#16328)
- rank `54` score `42` (heur `35`, lancedb `7`) #16208: Core: Cache PartitionData template in PartitionsTable to avoid rebuilding Avro schema per partition (#16208)
- rank `71` score `37` (heur `32`, lancedb `5`) #16287: CI: Make CVE scan blocking on PRs, informational on main (#16287)
- rank `95` score `19` (heur `12`, lancedb `7`) #16368: Website: remove duplicated entries from search (#16368)

### False Positives In Top 10

- score `92` #16108: Core: Support pluggable executor service for manifest writing on SnapshotUpdate (#16108)
- score `84` #14122: Spark: Remove Spark 3.4 support (#14122)
- score `73` #16447: Flink: Backport add column fix to flink v1.20, v2.0 (#16447)
