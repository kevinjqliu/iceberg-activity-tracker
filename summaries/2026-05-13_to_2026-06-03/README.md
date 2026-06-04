# Iceberg Community Sync Summary

- Period: `2026-05-13` to before `2026-06-03`
- Review candidates: `316`

## apache/iceberg

### Java

_Top 20 themes from 119 scored commits._

- Core, Parquet: Allow for Writing Parquet/Avro Manifests in V4 (#15634) (Thanks Russell Spitzer!)
- Flink: Support writing shredded variant (#15596) (Thanks GuoYu!)
- API, Core, Orc: Implement project() for partition statistics scan API (#16569) (Thanks gaborkaszab!)
- Spec: Add v4 content stats representation (#14234) (Thanks Eduard Tudenhoefner!)
- Core: Add V4 location relativization utilities (#16174) (Thanks Anoop Johnson!)
- OpenAPI: Add CatalogObjectIdentifier schema (#16144) (Thanks Steven Zhen Wu!)
- Core: Support pluggable executor service for manifest writing on SnapshotUpdate (#16108) (Thanks Hongyue and Steve Zhang!)
- Core: v4 table metadata location should be optional (#16572) (Thanks Alex Stephen and Anoop Johnson!)
- REST Spec: Add unregister table endpoint (#16400) (Thanks Ryan Blue and Claude Code (Opus 4.7, 1M context)!)
- [SPEC] Add relative paths to v4 spec (#15630) (Thanks Daniel Weeks and Talat Uyarer!)
- Flink: Support UUID type in Avro and Parquet readers and writers (#16097) (Thanks Joy Haldar!)
- Spark: Remove Spark 3.4 support (#14122) (Thanks Kevin Liu!)
- Flink: Use native slot sharing group inheritance for maintenance tasks (#16329) (Thanks GuoYu!)
- Flink: Fix ALTER TABLE to add column to specific position (#16419) (Thanks Stepan Stepanishchev!)
- Core, Orc: Remove deprecated partition stats read functionality (#14998) (Thanks gaborkaszab!)
- Flink: Allow setting slot sharing group for fine-grained resource management in DynamicSink (#16065) (Thanks Han You!)
- Core, Flink: Add UUID to DataTestBase SUPPORTED_PRIMITIVES (#16364) (Thanks Joy Haldar!)
- Spark: Also disable min/max aggregation push down for binary (#16328) (Thanks Dong Wang and Timothy Meehan!)
- Compaction and rewrite data files: expand rewrite planning and execution (#16219, #16593) (Thanks Varun Lakhyani!)
- Core: Cache PartitionData template in PartitionsTable to avoid rebuilding Avro schema per partition (#16208) (Thanks SevenJ!)

## apache/iceberg-python

### Python

_Top 17 themes from 58 scored commits._

- REST pagination: add pagination and page-size support for namespaces, tables, and views (#3347, #3348, #3349, #3377) (Thanks Yuya Ebihara and Kevin Liu!)
- Support `pa.RecordBatchReader` in Table.`{append,overwrite}` (#3335) (Thanks Paul Mathew!)
- fix(table): avoid committing update builders after exceptions (#3354) (Thanks Minh Vu!)
- Catalog views: add and expand view support (#3406, #3408) (Thanks Yuya Ebihara!)
- Add `@typing.override` to catalog and FileIO implementations (#3360) (Thanks vishnu prakash!)
- feat(cli): deprecate version command in favor of --version flag (#3206) (Thanks Chris Qiu and Kevin Liu!)
- Fix walrus truthiness on metrics bounds and identity-partition projection (#3412) (Thanks Kevin Liu!)
- docs: add Iceberg security model (#3425) (Thanks Sung Yun!)
- fix(fsspec): handle zero-byte files in `__len__` (#3353) (Thanks Minh Vu!)
- fix: avoid `TSaslClientTransport` reuse to eliminate server-side SASL noise (#3357) (Thanks barking-code!)
- feat(view): View object API (#3338) (Thanks Gabriel Igliozzi!)
- perf(add_files): stream manifest entries for duplicate-files check (#3287) (Thanks Ben Lai!)
- Reject empty `source-ids` in `PartitionField` / `SortField` (#3411) (Thanks Kevin Liu!)
- Add papermill-based tests for PyIceberg examples (#3330) (Thanks Federico!)
- REST: Rename rest-scan-planning-enabled to scan-planning-mode (#3376) (Thanks Yuya Ebihara!)
- Fix precision loss in large integral string conversions (#3405) (Thanks Minh Vu!)
- Make `View.sql_for` case-insensitive and return None for unknown dialect (#3407) (Thanks Yuya Ebihara!)

## apache/iceberg-rust

### Rust

_Top 19 themes from 58 scored commits._

- fix(puffin): add missing magic number validation for puffins (#2416) (Thanks dentiny!)
- feat!(runtime): Support custom Runtime in Catalog (#2308) (Thanks Shawn Chang and blackmwk!)
- Encryption: add key management and encrypted IO support (#2383, #2402) (Thanks Xander!)
- Infra: add bindings/python into root workspace (#2506) (Thanks Kevin Liu!)
- feat: HuggingFace Hub storage backend and CDC table properties (#2375) (Thanks Krisztián Szűcs!)
- fix(spec): support JSON binary literals (#2476) (Thanks Minh Vu!)
- docs: add Iceberg security model (#2524) (Thanks Sung Yun!)
- fix(transaction): preserve delete-only manifests in FastAppend (#2545) (Thanks Liang-Chi Hsieh!)
- fix(spec): don't panic on overwrite-truncate when previous totals exceed i32::MAX or are non-numeric (#2511) (Thanks Sreeram Garlapati and Aman Rawat!)
- chore(spec): remove stale #[allow(dead_code)] from snapshot_summary (#2514) (Thanks Sreeram Garlapati!)
- Fix pyiceberg-core dev dependency resolution (#2442) (Thanks Kevin Liu!)
- Use cargo publish to publish crates (#2489) (Thanks blackmwk!)
- chore(ci): omit blanket/auto-trait/auto-derived impls from public API (#2542) (Thanks Xander!)
- Add Hugging Face storage option to storage/opendal/README (#2487) (Thanks Quentin Lhoest!)
- feat(iceberg): log warning when available_parallelism falls back to default (#2520) (Thanks Xin Huang!)
- Ignore RUSTSEC-2024-0014 (#2531) (Thanks blackmwk!)
- feat(partition): adjust transform boundary for timestamp types (#2422) (Thanks dentiny!)
- feat(arrow): pass `&FieldRef` instead of `&Field` in `ArrowSchemaVisitor` to achieve cheap clone (#2471) (Thanks Liang Gong!)
- Add Spice.ai to Users (#2516) (Thanks Luke Kim!)

## apache/iceberg-go

### Go

_Top 20 themes from 54 scored commits._

- Deletion vectors: add read, write, and validation support (#1053, #1055, #1060, #1100, #1134) (Thanks Tanmay Rauth and Andrei Tserakhau!)
- feat(catalog): add PurgeTable as optional interface for physical file deletion (#1104) (Thanks Mithil Girish!)
- Row lineage: expand support for lineage-aware reads and writes (#1075, #1099) (Thanks Tanmay Rauth and Tobias Pütz!)
- feat(table/dv): accept partition spec and data on DVWriter.Add (#1136) (Thanks Andrei Tserakhau!)
- feat(table): MoR equality-rewrite - insert/reinsert writer API (#1120) (Thanks Tanmay Rauth!)
- fix(table): map nanosecond Arrow timestamps to v3 TimestampNs/TimestampTzNs types (#1081) (Thanks Jacob Marble!)
- feat: add variant type support (Iceberg v3) - non shredding (#932) (Thanks Neelesh Salian!)
- feat(table): emit null current-snapshot-id for empty v3 metadata (#1059) (Thanks Andrei Tserakhau!)
- fix(manifest): stop writing deprecated distinct_counts (field-id 111) (#1102) (Thanks Krutika Dhananjay and Matt Topol!)
- feat(table): Adding geometry and geography type + schema plumbing (#984) (Thanks David Zhao!)
- Encryption: add key management and encrypted IO support (#1069, #1088) (Thanks Andrei Tserakhau and Tanmay Rauth!)
- docs: add Iceberg security model (#1137) (Thanks Sung Yun!)
- feat(io): add ManagedIdentityCredential support for Azure (#1062) (Thanks Alessandro Nori!)
- feat(table): wire DVWriter into position-delete producer with property gating (#1113) (Thanks Tanmay Rauth!)
- perf(table): dedupe shared manifest reads during snapshot expiration (#1118) (Thanks Ondřej Pavela!)
- feat(table): add DV planning validations to match Java's DeleteFileIndex (#1050) (#1108) (Thanks Tanmay Rauth!)
- feat(cli): add branch create and tag create commands (#1068) (Thanks Tanmay Rauth!)
- feat(cli): add expire-snapshots command with dry-run (#1063) (Thanks Tanmay Rauth!)
- feat(cli): add snapshots and refs commands (#1072) (Thanks Tanmay Rauth!)
- feat(io): register oss scheme for aliyun oss S3-compatible storage (#1074) (Thanks Lei Zhang!)

## apache/iceberg-cpp

### C++

_Top 16 themes from 27 scored commits._

- feat(io): add bulk delete API to FileIO. (#659) (Thanks slfan1989!)
- feat: Add v3 timestamp nanosecond primitive types (#653) (Thanks Junwang Zhao!)
- feat(manifest): add ManifestFilterManager and ManifestMergeManager (#652) (Thanks Guotao Yu!)
- feat(puffin): add puffin file reader and writer (#624) (Thanks ZhaoXuan!)
- feat(data): add MOR file scan task reader (#657) (Thanks Gang Wu!)
- feat: add IncrementalFileCleanup strategy and dispatch in ExpireSnapshots::Finalize (#648) (Thanks Xinli Shang, shangxinli, and Claude Opus 4.6!)
- docs: add Iceberg security model (#688) (Thanks Sung Yun!)
- fix: evaluate ManifestGroup file filters (#664) (Thanks Minh Vu!)
- fix(parquet): fix parquet writer metrics conversion (#681) (Thanks Gang Wu!)
- fix: preserve snapshot ID width in UseRef (#661) (Thanks Minh Vu!)
- feat: metrics for parquet writer (#651) (Thanks wzhuo!)
- refactor: move temporal utilities out of transform util (#675) (Thanks Junwang Zhao!)
- fix(parquet): check compression codec availability (#656) (Thanks Gang Wu!)
- fix: disallow zoned and non-zoned literal comparisons (#676) (Thanks Junwang Zhao!)
- feat(data): coalesce position deletes into range inserts (#645) (Thanks Sebastian Baunsgaard!)
- fix: correct StrictMetricsEvaluator::CanContainNulls/CanContainNaNs when field missing from stats map (#686) (Thanks Yingfan Guo!)
