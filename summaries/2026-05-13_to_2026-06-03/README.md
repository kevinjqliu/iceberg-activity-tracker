# Iceberg Community Sync Summary

- Period: `2026-05-13` to before `2026-06-03`
- Review candidates: `316`

## apache/iceberg

### Java

_Top 20 themes from 119 scored commits._

- Top themes: `20`
- Commits covered by top themes: `21`
- Other reviewable commits: `54`
- Suppressed commits: `44`

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

### Other Reviewable Commits

- CI: Make CVE scan blocking on PRs, informational on main (#16287) (Thanks Kevin Liu!)
- Spark: Trim TestStructuredStreamingRead3 parameter rows from 8 to 2 (#16559) (Thanks Steven Zhen Wu and Claude Opus 4.7 (1M context)!)
- Core: Use ArrayList for manifest list materialization (#15640) (Thanks Manu Zhang!)
- Flink: Refresh table in ListMetadataFiles to prevent incorrect orphan file deletion (#16324) (Thanks Anupam Yadav!)
- Flink: Fix duplicate commits in DynamicCommitter when Flink jobId changes on restart (#16011) (Thanks lrsb!)
- Flink: Add decimal write/read roundtrip test for FlinkParquetReaders (#16346) (Thanks Vova Kolmakov!)
- Flink: Backport Use native slot sharing group inheritance for maintenance tasks to 2.0 and 1.20 (#16337) (Thanks GuoYu!)
- Spark: Backport Add _row_id and _last_updated_sequence_number raeder in Orc to support lineage (#16534) (Thanks GuoYu!)
- Flink: Backport support UUID type in Avro and Parquet readers and writers (#16333) (Thanks Joy Haldar!)
- Spark: Disable min/max aggregation push down for string under any mode (#16320) (Thanks Dong Wang!)
- Flink: Honor schema identifier fields in dynamic-sink record routing (#16243) (Thanks Jordan Epstein!)
- Core: Fix NPE in RemoveOrphanFiles with prefix_listing for root table location(#16351) (Thanks liuliquan-marshal!)
- Spark 4.1: Add session configs for adaptive split sizing and parallelism (#16088) (Thanks Karuppayya!)
- Core: Fix optionalOAuthParams dropped during non-exchange token refresh (#16022) (#16023) (Thanks Bharath Krishna!)
- Core: Fix ByteBufferInputStream.read() to return -1 at EOF (#16167) (Thanks Sachin Ranjalkar!)
- Flink: Fix flaky TestMonitorSource.testStateRestore (#16548) (Thanks Vova Kolmakov!)
- Core: Fix SerializableTable.sortOrders() throwing on historical sort orders with dropped fields (#16519) (#16521) (Thanks Yong Zheng!)
- Core: Validate non-string elements in JsonUtil.getStringArray (#16586) (Thanks Steven Zhen Wu and Claude Opus 4.7 (1M context)!)
- Spark: Deprecate SparkFilters in favor of SparkV2Filters (#16616) (Thanks Huaxin Gao and Cursor!)
- Flink: Nanosecond gaps in SortKeySerializer and ColumnStatsWatermarkExtractor for v2.0 (#16322) (Thanks Talat UYARER!)
- Flink: Nanosecond gaps in SortKeySerializer and ColumnStatsWatermarkExtractor (#16268) (Thanks Talat UYARER!)
- Flink: Backport add column fix to flink v1.20, v2.0 (#16447) (Thanks Stepan Stepanishchev!)
- Flink: Nanosecond gaps in SortKeySerializer and ColumnStatsWatermarkExtractor for 1.20 (#16323) (Thanks Talat UYARER!)
- Docs: Publish Iceberg security model (#16538) (Thanks Sung Yun!)
- Website: remove duplicated entries from search (#16368) (Thanks Maksim Konstantinov!)
- Arrow: Fix vectorized reads of decimal columns with default values (#16501) (Thanks Hao Jiang!)
- Core: Replace deprecated CloseableHttpClient.execute (#16149) (Thanks Yuya Ebihara!)
- Core: Remove redundant string concatenation (#16409) (Thanks Yuya Ebihara!)
- Core: Skip testAddManyFilesWithConsistentOrdering if WORKER_THREAD_POOL_SIZE < 3 (#16506) (Thanks Yuya Ebihara!)
- Flink: Handle table comments in FlinkSQL (#16423) (Thanks Stepan Stepanishchev!)
- Spec: Clarify non-default CRS conventions (#15834) (Thanks Milan Stefanovic!)
- Encrypting IO as a `DelegateFileIO` (#14876) (Thanks Sreesh Maheshwar!)
- Arrow: Fix ClassCastException in vectorized reader on int-to-long pro… (#16343) (Thanks Xiening Dai!)
- Parquet: Fix timestamp_ns and timestamptz_ns predicate pushdown (#16619) (Thanks Vova Kolmakov!)
- Kafka Connect: Fix ConcurrentModificationException in IcebergSinkConfig.tableConfig (#16438) (Thanks Vova Kolmakov!)
- Arrow: Fix truncation of decimals with precision larger than 18 (#16627) (Thanks Vova Kolmakov!)
- fix int96 timestamp offset in arrow dictionary decode (#16435) (Thanks Sung Yun!)
- Kafka Connect: Add end-to-end test for commit failure propagation (#16432) (Thanks Anupam Yadav!)
- Site: Add version URL alias hook for docs (#16496) (Thanks Kevin Liu!)
- Close metrics reporter in RESTSessionCatalog and add test in CatalogTests (#16310) (Thanks Talat UYARER!)
- Spark: Backport migrate SparkCopyOnWriteScan to SupportsRuntimeV2Filtering (#16303) (Thanks drexler-sky and Kevin Liu!)
- Doap: Update DOAP to reference 1.11.0 (#16415) (Thanks Aihua Xu!)
- Flink: Backport DynamicCommitter jobId fix to v1.20 and v2.0 (#16648) (Thanks lrsb!)
- Doap: Update Doap to reference 1.10.2 (#16405) (Thanks Amogh Jahagirdar!)
- iceberg go 0.6.0 release blog (#16649) (Thanks Neelesh Salian!)
- Data: Remove Flag FEATURE_META_ROW_LINEAGE in BaseFormatModelTests (#16529) (Thanks GuoYu!)
- Kafka Connect: Surface commit failures instead of silently swallowing them (#16237) (Thanks Anupam Yadav!)
- Spark: Backport #16088 to Spark 3.4, 3.5, 4.0 (#16344) (Thanks Karuppayya and karuppayya!)
- Flink: Backport honor schema identifier fields in dynamic-sink record routing (#16597) (Thanks Jordan Epstein!)
- Flink: Backport PR #16324 to v2.0 and v1.20 (#16338) (Thanks Kevin Liu, copilot-swe-agent[bot], and kevinjqliu!)
- Spark 4.1: Upgrade to Spark 4.1.2 (#16365) (Thanks Manu Zhang!)
- Flink: Backport handle table comments in FlinkSQL (#16503) (Thanks Stepan Stepanishchev!)
- Backport #16065 to Flink v2.0 and v1.20 (#16429) (Thanks Han You!)
- Spark: Backport aggregate pushdown tests with NaN's (#16316) (Thanks Vrishabh!)

### Suppressed Commits

- Add `.claude/` to .gitignore (#16533) (Thanks Xiening Dai!)
- Docs: Fix duplicate search results by moving versioned docs out of docs_dir (#16371) (Thanks Kevin Liu!)
- ci: only run site-ci deploy job for apache/iceberg (#16535) (Thanks Kevin Liu!)
- Build: Use major.minor versions in runtime-deps baselines (#16233) (Thanks Kevin Liu!)
- Build: Fix order in revapi.yml (#16511) (Thanks gaborkaszab!)
- infra: add 1.11.0 to issue template (#16413) (Thanks Aihua Xu!)
- infra: add 1.10.2 to issue template (#16404) (Thanks Amogh Jahagirdar!)
- Build: Ban Preconditions.checkState with %d placeholder (#16407) (Thanks Yuya Ebihara!)
- Docs: Drop manual deploy step from release instructions (#16495) (Thanks Steven Zhen Wu, Claude Opus 4.7 (1M context), and Kevin Liu!)
- Build: Designate a single Gradle cache writer across CI workflows (#16356) (Thanks Kevin Liu!)
- CI: Skip spotlessCheck in core-tests (#16505) (Thanks Yuya Ebihara!)
- Docs: Update information about metrics mode (#16391) (Thanks Vrishabh!)
- Docs: switch default docs version from nightly to latest (#16398) (Thanks Maksim Konstantinov!)
- Docs: Document adaptive split sizing configurations (Thanks Pratham Manja!)
- Build: Let revapi compare against 1.11.0 (#16412) (Thanks Aihua Xu!)
- Spark: Trim row-level test parameter rows from 6 to 3 (#16549) (Thanks Steven Zhen Wu and Claude Opus 4.7 (1M context)!)
- Core: Fix flaky test by ensuring generateContentLength returns positive value (#16539) (Thanks sanshi and shisan!)
- Docs: Add release notes for 1.11.0 (#16431) (Thanks Aihua Xu!)
- Docs: add more to 1.10.2 release notes (#16410) (Thanks Kevin Liu!)
- Docs: Add release notes for 1.10.2 (#16406) (Thanks Amogh Jahagirdar!)
- Build: Speed up Spark CI with parallel test execution (#16357) (Thanks Kevin Liu!)
- Build: Bump com.google.cloud:libraries-bom from 26.80.0 to 26.81.0 (#16382) (Thanks Huaxin Gao!)
- Build: Bump com.azure:azure-sdk-bom from 1.3.6 to 1.3.7 (#16637) (Thanks Yuya Ebihara and dependabot[bot]!)
- Build: Bump gradle-wrapper from 8.14.4 to 8.14.5 (#16381) (Thanks Huaxin Gao!)
- Build: Bump software.amazon.awssdk:bom from 2.44.7 to 2.44.12 (#16634) (Thanks dependabot[bot]!)
- Build: Bump docker/setup-buildx-action from 4.0.0 to 4.1.0 (#16632) (Thanks dependabot[bot]!)
- Build: Bump docker/build-push-action from 7.1.0 to 7.2.0 (#16631) (Thanks dependabot[bot]!)
- Build: Bump actions/stale from 10.2.0 to 10.3.0 (#16630) (Thanks dependabot[bot]!)
- Build: Bump openapi-spec-validator from 0.8.5 to 0.9.0 (#16629) (Thanks dependabot[bot]!)
- Build: Bump github/codeql-action from 4.35.5 to 4.36.0 (#16635) (Thanks dependabot[bot]!)
- Build: Bump org.immutables:value from 2.12.1 to 2.12.2 (#16636) (Thanks dependabot[bot]!)
- Build: Bump io.netty:netty-buffer from 4.2.13.Final to 4.2.14.Final (#16628) (Thanks dependabot[bot]!)
- Build: Bump com.google.cloud:libraries-bom from 26.81.0 to 26.83.0 (#16551) (Thanks dependabot[bot]!)
- Build: Bump zizmorcore/zizmor-action from 0.5.3 to 0.5.6 (#16550) (Thanks dependabot[bot]!)
- Build: Bump slf4j from 2.0.17 to 2.0.18 (#16553) (Thanks dependabot[bot]!)
- Build: Bump com.diffplug.spotless:spotless-plugin-gradle (#16552) (Thanks dependabot[bot]!)
- Build: Bump github/codeql-action from 4.35.4 to 4.35.5 (#16554) (Thanks dependabot[bot]!)
- Build: Bump software.amazon.awssdk:bom from 2.44.4 to 2.44.7 (#16555) (Thanks dependabot[bot]!)
- Build: Bump actions/labeler from 6.0.1 to 6.1.0 (#16378) (Thanks dependabot[bot]!)
- Build: Bump github/codeql-action from 4.35.1 to 4.35.4 (#16375) (Thanks dependabot[bot]!)
- Build: Bump org.xerial:sqlite-jdbc from 3.53.0.0 to 3.53.1.0 (#16379) (Thanks dependabot[bot]!)
- Build: Bump jetty from 12.1.8 to 12.1.9 (#16374) (Thanks dependabot[bot]!)
- Build: Bump datamodel-code-generator from 0.56.1 to 0.57.0 (#16373) (Thanks dependabot[bot]!)
- Build: Bump pymarkdownlnt from 0.9.36 to 0.9.37 (#16372) (Thanks dependabot[bot]!)

## apache/iceberg-python

### Python

_Top 17 themes from 58 scored commits._

- Top themes: `17`
- Commits covered by top themes: `21`
- Other reviewable commits: `0`
- Suppressed commits: `37`

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

### Suppressed Commits

- docs: fix New York longitude sign in partial overwrite example (#3403) (Thanks Minh Vu!)
- Test: Replace rest-scan-planning-enabled with scan-planning-mode (#3391) (Thanks Yuya Ebihara!)
- Build: Update actions/upload-artifact to v7.0.1 (#3401) (Thanks Yuya Ebihara!)
- Fix typo (#3424) (Thanks Yuya Ebihara!)
- Fix typo in `test_add_files` (#3378) (Thanks Yuya Ebihara!)
- Chore: Updated PyArrow Dependencies (#3362) (Thanks CalebWeisgerber!)
- Build: Bump pyiceberg-core from 0.9.0 to 0.9.1 (#3370) (Thanks dependabot[bot]!)
- Build: Bump prek from 0.3.13 to 0.4.0 (#3400) (Thanks dependabot[bot]!)
- Build: Bump pydantic from 2.13.3 to 2.13.4 (#3369) (Thanks dependabot[bot]!)
- Build: Bump idna from 3.11 to 3.15 (#3386) (Thanks dependabot[bot]!)
- Build: Bump daft from 0.7.13 to 0.7.14 (#3434) (Thanks dependabot[bot]!)
- Build: Bump zizmorcore/zizmor-action from 0.5.3 to 0.5.6 (#3432) (Thanks dependabot[bot]!)
- Build: Bump prek from 0.4.0 to 0.4.1 (#3433) (Thanks dependabot[bot]!)
- Build: Bump click from 8.3.3 to 8.4.1 (#3435) (Thanks dependabot[bot]!)
- Build: Bump bodo from 2026.4 to 2026.5 (#3437) (Thanks dependabot[bot]!)
- Build: Bump cachetools from 7.1.1 to 7.1.4 (#3438) (Thanks dependabot[bot]!)
- Build: Bump huggingface-hub from 1.15.0 to 1.16.1 (#3439) (Thanks dependabot[bot]!)
- Build: Bump duckdb from 1.5.2 to 1.5.3 (#3440) (Thanks dependabot[bot]!)
- Build: Bump actions/stale from 10.2.0 to 10.3.0 (#3431) (Thanks dependabot[bot]!)
- Build: Bump github/codeql-action from 4.35.5 to 4.36.0 (#3430) (Thanks dependabot[bot]!)
- Build: Bump daft from 0.7.10 to 0.7.13 (#3399) (Thanks dependabot[bot]!)
- Build: Bump mypy-boto3-glue from 1.43.5 to 1.43.8 (#3398) (Thanks dependabot[bot]!)
- Build: Bump requests from 2.33.1 to 2.34.2 (#3397) (Thanks dependabot[bot]!)
- Build: Bump google-auth from 2.52.0 to 2.53.0 (#3396) (Thanks dependabot[bot]!)
- Build: Bump thrift from 0.22.0 to 0.23.0 (#3395) (Thanks dependabot[bot]!)
- Build: Bump huggingface-hub from 1.14.0 to 1.15.0 (#3394) (Thanks dependabot[bot]!)
- Build: Bump github/codeql-action from 4.35.4 to 4.35.5 (#3393) (Thanks dependabot[bot]!)
- Build: Bump pymdown-extensions from 10.16.1 to 10.21.3 (#3385) (Thanks dependabot[bot]!)
- Build: Bump adlfs from 2026.4.0 to 2026.5.0 (#3375) (Thanks dependabot[bot]!)
- Build: Bump prek from 0.3.11 to 0.3.13 (#3374) (Thanks dependabot[bot]!)
- Build: Bump mypy-boto3-glue from 1.43.0 to 1.43.5 (#3373) (Thanks dependabot[bot]!)
- Build: Bump ipykernel from 7.1.0 to 7.2.0 (#3372) (Thanks dependabot[bot]!)
- Build: Bump google-auth from 2.50.0 to 2.52.0 (#3371) (Thanks dependabot[bot]!)
- Build: Bump huggingface-hub from 1.13.0 to 1.14.0 (#3368) (Thanks dependabot[bot]!)
- Build: Bump cachetools from 7.1.0 to 7.1.1 (#3367) (Thanks dependabot[bot]!)
- Build: Bump github/codeql-action from 4.35.3 to 4.35.4 (#3366) (Thanks dependabot[bot]!)
- Build: Bump urllib3 from 2.6.3 to 2.7.0 (#3352) (Thanks dependabot[bot]!)

## apache/iceberg-rust

### Rust

_Top 19 themes from 58 scored commits._

- Top themes: `19`
- Commits covered by top themes: `20`
- Other reviewable commits: `0`
- Suppressed commits: `38`

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

### Suppressed Commits

- feat(ci): add cargo-public-api checks for public API stability (#2525) (Thanks Xander!)
- Add some scripts to help release (#2522) (Thanks blackmwk!)
- docs: add pyiceberg-core release validation (#2502) (Thanks Asish Kumar!)
- chore: add `uv` to dependabot for /bindings/python (#2444) (Thanks Kevin Liu!)
- chore: Add a lock check to CI (#2484) (Thanks Xander!)
- ci: add check_standalone job to verify each crate compiles independently (#2389) (Thanks Kevin Liu and Copilot!)
- ci(toml): check toml fmt (#2504) (Thanks Liang Gong!)
- chore: update deps for /bindings/python (#2445) (Thanks Kevin Liu!)
- chore(deps): Bump urllib3 from 2.6.3 to 2.7.0 in /bindings/python (#2523) (Thanks dependabot[bot]!)
- chore(deps-dev): Bump maturin from 1.13.2 to 1.13.3 in /bindings/python (#2495) (Thanks dependabot[bot]!)
- chore(deps): Bump idna from 3.13 to 3.15 in /bindings/python (#2470) (Thanks dependabot[bot]!)
- chore(deps-dev): Bump pytest from 8.4.2 to 9.0.3 in /bindings/python (#2326) (Thanks dependabot[bot] and blackmwk!)
- chore(deps): Bump urllib3 from 2.6.3 to 2.7.0 in /bindings/python (#2434) (Thanks dependabot[bot]!)
- chore(deps-dev): Bump maturin from 1.13.1 to 1.13.2 in /bindings/python (#2458) (Thanks dependabot[bot]!)
- chore(deps): Bump taiki-e/install-action from 2.77.4 to 2.79.7 (#2547) (Thanks dependabot[bot]!)
- chore(deps): Bump crate-ci/typos from 1.46.2 to 1.46.3 (#2548) (Thanks dependabot[bot]!)
- chore(deps): Bump actions/stale from 10.2.0 to 10.3.0 (#2549) (Thanks dependabot[bot]!)
- chore(deps): Bump the arrow-parquet group with 2 updates (#2551) (Thanks dependabot[bot] and blackmwk!)
- chore(deps): Bump dashmap from 6.1.0 to 6.2.1 (#2552) (Thanks dependabot[bot] and blackmwk!)
- chore(deps): Bump github/codeql-action from 4.35.5 to 4.36.0 (#2553) (Thanks dependabot[bot]!)
- chore(deps): Bump reqwest from 0.12.28 to 0.13.3 (#2554) (Thanks dependabot[bot]!)
- chore(deps): Bump minijinja from 2.19.0 to 2.20.0 (#2555) (Thanks dependabot[bot]!)
- chore(deps): Bump the arrow-parquet group across 1 directory with 6 updates (#2496) (Thanks dependabot[bot]!)
- chore(deps): Bump reqwest from 0.12.28 to 0.13.3 (#2498) (Thanks dependabot[bot] and blackmwk!)
- chore(deps): Bump github/codeql-action from 4.35.4 to 4.35.5 (#2497) (Thanks dependabot[bot]!)
- chore(deps): Bump zizmorcore/zizmor-action from 0.5.3 to 0.5.6 (#2494) (Thanks dependabot[bot]!)
- chore(deps): Bump peaceiris/actions-gh-pages from 4.0.0 to 4.1.0 (#2493) (Thanks dependabot[bot]!)
- chore(deps): Bump taiki-e/install-action from 2.77.4 to 2.79.0 (#2492) (Thanks dependabot[bot]!)
- chore(deps): Bump crate-ci/typos from 1.46.1 to 1.46.2 (#2491) (Thanks dependabot[bot]!)
- chore(deps): Bump serde_with from 3.19.0 to 3.20.0 (#2499) (Thanks dependabot[bot]!)
- chore(deps): Bump github/codeql-action from 4.35.3 to 4.35.4 (#2457) (Thanks dependabot[bot]!)
- chore(deps): Bump crate-ci/typos from 1.46.0 to 1.46.1 (#2459) (Thanks dependabot[bot]!)
- chore(deps): Bump reqwest from 0.12.28 to 0.13.3 (#2460) (Thanks dependabot[bot]!)
- chore(deps): Bump taiki-e/install-action from 2.77.1 to 2.77.4 (#2461) (Thanks dependabot[bot]!)
- chore(deps): Bump the arrow-parquet group with 2 updates (#2448) (Thanks dependabot[bot] and Shawn Chang!)
- chore(deps): Bump taiki-e/install-action from 2.75.30 to 2.77.1 (#2446) (Thanks dependabot[bot]!)
- chore(deps): Bump rand from 0.9.4 to 0.10.1 (#2449) (Thanks dependabot[bot]!)
- chore(deps): Bump reqwest from 0.12.28 to 0.13.3 (#2450) (Thanks dependabot[bot]!)

## apache/iceberg-go

### Go

_Top 20 themes from 54 scored commits._

- Top themes: `20`
- Commits covered by top themes: `26`
- Other reviewable commits: `16`
- Suppressed commits: `12`

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

### Other Reviewable Commits

- feat(table): reject AddDataFiles on v3 when first_row_id is missing (#1000) (#1101) (Thanks Tanmay Rauth!)
- Skip DELETED tombstones in DeleteOrphanFiles' referenced set (#1076) (Thanks Krutika Dhananjay!)
- feat(cli): add clean-orphan-files command (#1066) (Thanks Tanmay Rauth!)
- feat(cli): add --show-defaults flag to schema command (#1067) (Thanks Tanmay Rauth!)
- fix(table): tighten strict negative metrics checks (#1106) (Thanks Minh Vu!)
- fix(table): handle missing strict metrics conservatively (#1098) (Thanks Minh Vu!)
- fix(table): release Arrow chunks on GetRecords error paths (#1093) (Thanks Andrei Tserakhau!)
- fix(table): derive position-delete partition paths from table schema (#1089) (Thanks Andrei Tserakhau!)
- feat(table): project reserved row-lineage fields as null when the file lacks them (#1045) (Thanks David Zhao!)
- feat(cli): add upgrade and rollback commands (#1071) (Thanks Tanmay Rauth!)
- fix(substrait): emit decimal literals as 16-byte little-endian (#1130) (Thanks Andrei Tserakhau!)
- fix(substrait): use bound field precision in toDecimalLiteral (#1028) (#1121) (Thanks Masa!)
- fix: reject invalid transform widths (#1110) (Thanks Minh Vu!)
- fix(test): TestCreateTable existence check failure (#1105) (Thanks Andrei Tserakhau!)
- Fix Azure credential test that fails when az is logged in (#1095) (Thanks Kevin Liu!)
- refactor: Slight refactor of the integration test (#355) (Thanks Fokko Driesprong!)

### Suppressed Commits

- test(table): add cross-client DV format compliance tests (#1131) (Thanks Tanmay Rauth!)
- fix(table): restore Summary/ColumnSizes test expectations to arrow-go v18.6.0 (#1114) (Thanks Matt Topol!)
- test(table): geospatial test fixtures (#1094) (Thanks Colton Loftus!)
- build(deps): bump the gomod_updates group with 5 updates (#1146) (Thanks dependabot[bot]!)
- build(deps): bump the gomod_updates group with 5 updates (#1123) (Thanks dependabot[bot]!)
- build(deps): bump github.com/containerd/containerd/v2 from 2.2.2 to 2.2.4 (#1116) (Thanks dependabot[bot]!)
- build(deps): bump the gomod_updates group with 3 updates (#1085) (Thanks dependabot[bot]!)
- build(deps): bump peaceiris/actions-gh-pages from 4.0.0 to 4.1.0 (#1122) (Thanks dependabot[bot]!)
- build(deps): bump github/codeql-action from 4.35.4 to 4.35.5 (#1124) (Thanks dependabot[bot]!)
- build(deps): bump zizmorcore/zizmor-action from 0.5.3 to 0.5.6 (#1125) (Thanks dependabot[bot]!)
- build(deps): bump actions/labeler from 6.0.1 to 6.1.0 (#1083) (Thanks dependabot[bot]!)
- build(deps): bump github/codeql-action from 4.35.3 to 4.35.4 (#1084) (Thanks dependabot[bot]!)

## apache/iceberg-cpp

### C++

_Top 16 themes from 27 scored commits._

- Top themes: `16`
- Commits covered by top themes: `16`
- Other reviewable commits: `0`
- Suppressed commits: `11`

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

### Suppressed Commits

- build(hive): add ICEBERG_BUILD_HIVE option and skeleton (#689) (Thanks liuxiaoyu!)
- fix(ci): fix macOS ci to use provided fmt (#670) (Thanks slfan1989!)
- fix(meson): add missing install headers for meson (#684) (Thanks Gang Wu!)
- ci: update pre-commit workflow permissions to write (#683) (Thanks Guotao Yu!)
- chore(ci): skip actions for draft PRs (#680) (Thanks Junwang Zhao!)
- build: sync Meson project version with CMake (#655) (Thanks slfan1989!)
- chore(doc): bump minimum Clang version to 18 (#695) (Thanks Junwang Zhao!)
- chore(deps): bump github/codeql-action from 4.35.5 to 4.36.0 (#691) (Thanks dependabot[bot]!)
- chore(deps): bump zizmorcore/zizmor-action from 0.5.3 to 0.5.6 (#678) (Thanks dependabot[bot]!)
- chore(deps): bump github/codeql-action from 4.35.4 to 4.35.5 (#677) (Thanks dependabot[bot]!)
- chore(deps): bump github/codeql-action from 4.35.3 to 4.35.4 (#654) (Thanks dependabot[bot]!)
