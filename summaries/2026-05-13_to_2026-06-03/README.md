# Iceberg Community Sync Summary

- Period: `2026-05-13` to before `2026-06-03`
- Review candidates: `235`

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
- Spark: Trim row-level test parameter rows from 6 to 3 (#16549) (Thanks Steven Zhen Wu and Claude Opus 4.7 (1M context)!)
- Core, Flink: Add UUID to DataTestBase SUPPORTED_PRIMITIVES (#16364) (Thanks Joy Haldar!)

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
- Add papermill-based tests for PyIceberg examples (#3330) (Thanks Federico!)
- REST: Rename rest-scan-planning-enabled to scan-planning-mode (#3376) (Thanks Yuya Ebihara!)
- Fix precision loss in large integral string conversions (#3405) (Thanks Minh Vu!)
- fix: avoid `TSaslClientTransport` reuse to eliminate server-side SASL noise (#3357) (Thanks barking-code!)
- feat(view): View object API (#3338) (Thanks Gabriel Igliozzi!)
- Fix typo (#3424) (Thanks Yuya Ebihara!)

## apache/iceberg-rust

### Rust

_Top 20 of 58 scored commits._

- feat!(runtime): Support custom Runtime in Catalog (#2308) (Thanks Shawn Chang and blackmwk!)
- feat(ci): add cargo-public-api checks for public API stability (#2525) (Thanks Xander!)
- Add some scripts to help release (#2522) (Thanks blackmwk!)
- Infra: add bindings/python into root workspace (#2506) (Thanks Kevin Liu!)
- feat(encryption) [5/N] Support encryption: Encryption Manager (#2383) (Thanks Xander!)
- docs: add Iceberg security model (#2524) (Thanks Sung Yun!)
- fix(transaction): preserve delete-only manifests in FastAppend (#2545) (Thanks Liang-Chi Hsieh!)
- feat(encryption) [6/N] support `ArrowReaderOptions` in `get_metadata` (#2402) (Thanks Xander!)
- feat: HuggingFace Hub storage backend and CDC table properties (#2375) (Thanks Krisztián Szűcs!)
- chore: Add a lock check to CI (#2484) (Thanks Xander!)
- Fix pyiceberg-core dev dependency resolution (#2442) (Thanks Kevin Liu!)
- fix(puffin): add missing magic number validation for puffins (#2416) (Thanks dentiny!)
- fix(spec): support JSON binary literals (#2476) (Thanks Minh Vu!)
- docs: add pyiceberg-core release validation (#2502) (Thanks Asish Kumar!)
- Add Hugging Face storage option to storage/opendal/README (#2487) (Thanks Quentin Lhoest!)
- Use cargo publish to publish crates (#2489) (Thanks blackmwk!)
- ci: add check_standalone job to verify each crate compiles independently (#2389) (Thanks Kevin Liu and Copilot!)
- Add Spice.ai to Users (#2516) (Thanks Luke Kim!)
- chore: add `uv` to dependabot for /bindings/python (#2444) (Thanks Kevin Liu!)
- fix(spec): don't panic on overwrite-truncate when previous totals exceed i32::MAX or are non-numeric (#2511) (Thanks Sreeram Garlapati and Aman Rawat!)
