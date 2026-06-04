# Iceberg Community Sync Summary

- Period: `2026-05-13` to before `2026-06-03`
- Review candidates: `289`

## apache/iceberg

### Java

_Top 20 of 119 scored commits._

- Core, Parquet: Allow for Writing Parquet/Avro Manifests in V4 (#15634) (Thanks Russell Spitzer!)
- Flink: Support writing shredded variant (#15596) (Thanks GuoYu!)
- API, Core, Orc: Implement project() for partition statistics scan API (#16569) (Thanks gaborkaszab!)
- Core: Add V4 location relativization utilities (#16174) (Thanks Anoop Johnson!)
- Spark: Trim row-level test parameter rows from 6 to 3 (#16549) (Thanks Steven Zhen Wu and Claude Opus 4.7 (1M context)!)
- Spec: Add v4 content stats representation (#14234) (Thanks Eduard Tudenhoefner!)
- OpenAPI: Add CatalogObjectIdentifier schema (#16144) (Thanks Steven Zhen Wu!)
- Core: Support pluggable executor service for manifest writing on SnapshotUpdate (#16108) (Thanks Hongyue and Steve Zhang!)
- Core: v4 table metadata location should be optional (#16572) (Thanks Alex Stephen and Anoop Johnson!)
- [SPEC] Add relative paths to v4 spec (#15630) (Thanks Daniel Weeks and Talat Uyarer!)
- Flink: Support UUID type in Avro and Parquet readers and writers (#16097) (Thanks Joy Haldar!)
- Flink: Backport Use native slot sharing group inheritance for maintenance tasks to 2.0 and 1.20 (#16337) (Thanks GuoYu!)
- Spark: Backport Add _row_id and _last_updated_sequence_number raeder in Orc to support lineage (#16534) (Thanks GuoYu!)
- Spark: Remove Spark 3.4 support (#14122) (Thanks Kevin Liu!)
- Flink: Backport support UUID type in Avro and Parquet readers and writers (#16333) (Thanks Joy Haldar!)
- Spark: Add compaction only benchmark - rewrite data files (#16219) (Thanks Varun Lakhyani!)
- Flink: Use native slot sharing group inheritance for maintenance tasks (#16329) (Thanks GuoYu!)
- Flink: Backport add column fix to flink v1.20, v2.0 (#16447) (Thanks Stepan Stepanishchev!)
- REST Spec: Add unregister table endpoint (#16400) (Thanks Ryan Blue and Claude Code (Opus 4.7, 1M context)!)
- Flink: Fix ALTER TABLE to add column to specific position (#16419) (Thanks Stepan Stepanishchev!)

## apache/iceberg-python

### Python

_Top 20 of 58 scored commits._

- Support `pa.RecordBatchReader` in Table.`{append,overwrite}` (#3335) (Thanks Paul Mathew!)
- fix(table): avoid committing update builders after exceptions (#3354) (Thanks Minh Vu!)
- REST: Add pagination support for list_tables (#3348) (Thanks Yuya Ebihara and Kevin Liu!)
- REST: Add support for page-size in list_namespaces, list_tables, and list_views (#3377) (Thanks Yuya Ebihara!)
- REST: Add pagination support for list_namespaces (#3347) (Thanks Yuya Ebihara and Kevin Liu!)
- REST: Add pagination support for `list_views` (#3349) (Thanks Yuya Ebihara!)
- feat(cli): deprecate version command in favor of --version flag (#3206) (Thanks Chris Qiu and Kevin Liu!)
- REST: Allow Identifier type in `drop_view` method (#3408) (Thanks Yuya Ebihara!)
- Add `@typing.override` to catalog and FileIO implementations (#3360) (Thanks vishnu prakash!)
- Fix walrus truthiness on metrics bounds and identity-partition projection (#3412) (Thanks Kevin Liu!)
- REST: Add integration test for views (#3406) (Thanks Yuya Ebihara!)
- docs: add Iceberg security model (#3425) (Thanks Sung Yun!)
- fix(fsspec): handle zero-byte files in `__len__` (#3353) (Thanks Minh Vu!)
- fix: avoid `TSaslClientTransport` reuse to eliminate server-side SASL noise (#3357) (Thanks barking-code!)
- perf(add_files): stream manifest entries for duplicate-files check (#3287) (Thanks Ben Lai!)
- Reject empty `source-ids` in `PartitionField` / `SortField` (#3411) (Thanks Kevin Liu!)
- Add papermill-based tests for PyIceberg examples (#3330) (Thanks Federico!)
- REST: Rename rest-scan-planning-enabled to scan-planning-mode (#3376) (Thanks Yuya Ebihara!)
- Fix precision loss in large integral string conversions (#3405) (Thanks Minh Vu!)
- feat(view): View object API (#3338) (Thanks Gabriel Igliozzi!)

## apache/iceberg-rust

### Rust

_Top 20 of 58 scored commits._

- fix(puffin): add missing magic number validation for puffins (#2416) (Thanks dentiny!)
- feat!(runtime): Support custom Runtime in Catalog (#2308) (Thanks Shawn Chang and blackmwk!)
- feat(ci): add cargo-public-api checks for public API stability (#2525) (Thanks Xander!)
- Add some scripts to help release (#2522) (Thanks blackmwk!)
- Infra: add bindings/python into root workspace (#2506) (Thanks Kevin Liu!)
- feat(encryption) [5/N] Support encryption: Encryption Manager (#2383) (Thanks Xander!)
- fix(spec): support JSON binary literals (#2476) (Thanks Minh Vu!)
- docs: add Iceberg security model (#2524) (Thanks Sung Yun!)
- fix(transaction): preserve delete-only manifests in FastAppend (#2545) (Thanks Liang-Chi Hsieh!)
- feat(encryption) [6/N] support `ArrowReaderOptions` in `get_metadata` (#2402) (Thanks Xander!)
- fix(spec): don't panic on overwrite-truncate when previous totals exceed i32::MAX or are non-numeric (#2511) (Thanks Sreeram Garlapati and Aman Rawat!)
- chore(spec): remove stale #[allow(dead_code)] from snapshot_summary (#2514) (Thanks Sreeram Garlapati!)
- feat: HuggingFace Hub storage backend and CDC table properties (#2375) (Thanks Krisztián Szűcs!)
- chore: Add a lock check to CI (#2484) (Thanks Xander!)
- Fix pyiceberg-core dev dependency resolution (#2442) (Thanks Kevin Liu!)
- docs: add pyiceberg-core release validation (#2502) (Thanks Asish Kumar!)
- Add Hugging Face storage option to storage/opendal/README (#2487) (Thanks Quentin Lhoest!)
- Use cargo publish to publish crates (#2489) (Thanks blackmwk!)
- ci: add check_standalone job to verify each crate compiles independently (#2389) (Thanks Kevin Liu and Copilot!)
- Add Spice.ai to Users (#2516) (Thanks Luke Kim!)

## apache/iceberg-go

### Go

_Top 20 of 54 scored commits._

- feat(table): add SerializeDV and DVWriter for deletion vector authoring (#1100) (Thanks Tanmay Rauth!)
- feat(catalog): add PurgeTable as optional interface for physical file deletion (#1104) (Thanks Mithil Girish!)
- feat(table/dv): accept partition spec and data on DVWriter.Add (#1136) (Thanks Andrei Tserakhau!)
- feat(table): scanner deletion-vector read path (#1053) (Thanks Andrei Tserakhau!)
- feat(table): preserve row lineage through copy-on-write rewrites (#1099) (Thanks Tanmay Rauth!)
- feat: add wire codec helpers for DataFile and FileScanTask (#1075) (Thanks Tobias Pütz!)
- feat(puffin): enforce required DV blob properties on write (#1060) (Thanks Andrei Tserakhau!)
- feat(puffin): validate deletion-vector blob header invariants on read (#1055) (Thanks Andrei Tserakhau!)
- feat: add variant type support (Iceberg v3) - non shredding (#932) (Thanks Neelesh Salian!)
- feat(table): emit null current-snapshot-id for empty v3 metadata (#1059) (Thanks Andrei Tserakhau!)
- fix(manifest): stop writing deprecated distinct_counts (field-id 111) (#1102) (Thanks Krutika Dhananjay and Matt Topol!)
- feat(table): MoR equality-rewrite - insert/reinsert writer API (#1120) (Thanks Tanmay Rauth!)
- fix(table): restore Summary/ColumnSizes test expectations to arrow-go v18.6.0 (#1114) (Thanks Matt Topol!)
- fix(table): map nanosecond Arrow timestamps to v3 TimestampNs/TimestampTzNs types (#1081) (Thanks Jacob Marble!)
- feat(cli): add branch create and tag create commands (#1068) (Thanks Tanmay Rauth!)
- feat(cli): add expire-snapshots command with dry-run (#1063) (Thanks Tanmay Rauth!)
- docs: add Iceberg security model (#1137) (Thanks Sung Yun!)
- feat(cli): add snapshots and refs commands (#1072) (Thanks Tanmay Rauth!)
- fix(table): release Arrow chunks on GetRecords error paths (#1093) (Thanks Andrei Tserakhau!)
- feat(cli): add clean-orphan-files command (#1066) (Thanks Tanmay Rauth!)
