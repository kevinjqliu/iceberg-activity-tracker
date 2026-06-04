# Iceberg Community Sync Summary

- Period: `2026-05-13` to before `2026-06-03`
- Review candidates: `177`

## apache/iceberg

### Java

_Top 20 of 119 scored commits._

- Core, Parquet: Allow for Writing Parquet/Avro Manifests in V4 (#15634) (Thanks Russell Spitzer!)
- Flink: Support writing shredded variant (#15596) (Thanks GuoYu!)
- API, Core, Orc: Implement project() for partition statistics scan API (#16569) (Thanks gaborkaszab!)
- Core: Add V4 location relativization utilities (#16174) (Thanks Anoop Johnson!)
- Spec: Add v4 content stats representation (#14234) (Thanks Eduard Tudenhoefner!)
- OpenAPI: Add CatalogObjectIdentifier schema (#16144) (Thanks Steven Zhen Wu!)
- Core: Support pluggable executor service for manifest writing on SnapshotUpdate (#16108) (Thanks Hongyue and Steve Zhang!)
- Core: v4 table metadata location should be optional (#16572) (Thanks Alex Stephen and Anoop Johnson!)
- [SPEC] Add relative paths to v4 spec (#15630) (Thanks Daniel Weeks and Talat Uyarer!)
- Flink: Support UUID type in Avro and Parquet readers and writers (#16097) (Thanks Joy Haldar!)
- Spark: Backport Add _row_id and _last_updated_sequence_number raeder in Orc to support lineage (#16534) (Thanks GuoYu!)
- Spark: Remove Spark 3.4 support (#14122) (Thanks Kevin Liu!)
- Flink: Backport support UUID type in Avro and Parquet readers and writers (#16333) (Thanks Joy Haldar!)
- Flink: Backport add column fix to flink v1.20, v2.0 (#16447) (Thanks Stepan Stepanishchev!)
- REST Spec: Add unregister table endpoint (#16400) (Thanks Ryan Blue and Claude Code (Opus 4.7, 1M context)!)
- Flink: Fix ALTER TABLE to add column to specific position (#16419) (Thanks Stepan Stepanishchev!)
- Core, Orc: Remove deprecated partition stats read functionality (#14998) (Thanks gaborkaszab!)
- Flink: Allow setting slot sharing group for fine-grained resource management in DynamicSink (#16065) (Thanks Han You!)
- Core, Flink: Add UUID to DataTestBase SUPPORTED_PRIMITIVES (#16364) (Thanks Joy Haldar!)
- Build: Bump github/codeql-action from 4.35.1 to 4.35.4 (#16375) (Thanks dependabot[bot]!)

## apache/iceberg-python

### Python

_Top 20 of 58 scored commits._

- Support `pa.RecordBatchReader` in Table.`{append,overwrite}` (#3335) (Thanks Paul Mathew!)
- REST: Add pagination support for list_tables (#3348) (Thanks Yuya Ebihara and Kevin Liu!)
- REST: Add support for page-size in list_namespaces, list_tables, and list_views (#3377) (Thanks Yuya Ebihara!)
- REST: Add pagination support for list_namespaces (#3347) (Thanks Yuya Ebihara and Kevin Liu!)
- REST: Add pagination support for `list_views` (#3349) (Thanks Yuya Ebihara!)
- REST: Allow Identifier type in `drop_view` method (#3408) (Thanks Yuya Ebihara!)
- fix(table): avoid committing update builders after exceptions (#3354) (Thanks Minh Vu!)
- Add `@typing.override` to catalog and FileIO implementations (#3360) (Thanks vishnu prakash!)
- feat(cli): deprecate version command in favor of --version flag (#3206) (Thanks Chris Qiu and Kevin Liu!)
- Fix walrus truthiness on metrics bounds and identity-partition projection (#3412) (Thanks Kevin Liu!)
- REST: Add integration test for views (#3406) (Thanks Yuya Ebihara!)
- docs: add Iceberg security model (#3425) (Thanks Sung Yun!)
- fix(fsspec): handle zero-byte files in `__len__` (#3353) (Thanks Minh Vu!)
- perf(add_files): stream manifest entries for duplicate-files check (#3287) (Thanks Ben Lai!)
- Build: Bump idna from 3.11 to 3.15 (#3386) (Thanks dependabot[bot]!)
- Add papermill-based tests for PyIceberg examples (#3330) (Thanks Federico!)
- REST: Rename rest-scan-planning-enabled to scan-planning-mode (#3376) (Thanks Yuya Ebihara!)
- Fix precision loss in large integral string conversions (#3405) (Thanks Minh Vu!)
- fix: avoid `TSaslClientTransport` reuse to eliminate server-side SASL noise (#3357) (Thanks barking-code!)
- feat(view): View object API (#3338) (Thanks Gabriel Igliozzi!)
