# Iceberg Community Sync Summary

- Period: `2026-04-22` to before `2026-05-13`
- Review candidates: `303`

## apache/iceberg

### Java

_Top 20 themes from 131 scored commits._

- Top themes: `20`
- Commits covered by top themes: `20`
- Other reviewable commits: `75`
- Suppressed commits: `36`

- Spark: Support writing shredded variant in Iceberg-Spark (#14297) (Thanks Aihua Xu and Neelesh Salian!)
- Core: Add implementations of v4 TrackedFile interfaces (#15854) (Thanks Anoop Johnson!)
- Core: Add builders for v4 structs (#16092) (Thanks Anoop Johnson and Eduard Tudenhoefner!)
- Core: Fix row ID assignment for EXISTING entry during a manifest merge (#16263) (Thanks Amogh Jahagirdar, ChengJi, and Russell Spitzer!)
- Core, Catalogs: Add support for unique table locations via catalog property (#12892) (Thanks Dmitriy Avseitsev!)
- Spark: Add unknown type support to Spark 3.4 and 3.5 (#16066) (Thanks Kurtis Wright!)
- Spark: Fix LICENSE/NOTICE compliance for all versions of spark-runtime (v3.4, v3.5, v4.0, v4.1) (#16215) (Thanks Kevin Liu!)
- Spark: Backport support writing shredded variant in Iceberg-Spark (#16241) (Thanks pvary!)
- AWS, GCP: add Kryo round-trip regression test for refreshed storage credentials (#16112) (Thanks Akshay Thorat!)
- Spark: Fix dropped file length in SerializableFileIOWithSize (#16284) (Thanks Ajay Yadav!)
- Flink: Add Nanosecond Precision Support for Flink-Iceberg Integration (#15475) (Thanks Talat UYARER!)
- Core: Add partition to TrackedFile (#16253) (Thanks Eduard Tudenhoefner!)
- Spark 3.4: Pass FileIO on Spark's read path (#16307) (Thanks Kevin Liu!)
- Core: Fix JdbcCatalog & InMemoryCatalog to prevent dropping parent namespaces with children (#16061) (Thanks sagib-sqream!)
- Flink: Fix JdbcLockFactory to allow ClientPoolImpl connection retry (#16049) (Thanks Anupam Yadav!)
- Core, AWS: Adapt code to S3 signing endpoint promotion (#15451) (Thanks Alexandre Dutra!)
- Kafka Connect: Add Trivy CVE scan to CI (#15430) (#15430) (Thanks Robin Moffatt and Claude Opus 4.6!)
- Spark, Hive: Fix snapshot procedure for tables with Variant columns (#15964) (Thanks Neelesh Salian!)
- ORC: Add _row_id and _last_updated_sequence_number raeder in Orc to support lineage (#15776) (Thanks GuoYu!)
- Spark 3.4: Support recursive delegate unwrapping to find ExtendedParser in parser chains (#16306) (Thanks Kevin Liu!)

### Other Reviewable Commits

- Spark: Support TimestampNTZ in SparkZOrderUDF (#15778) (Thanks milleniax and abdullin.marsel9!)
- Kafka Connect: Support VARIANT when record convert (#15283) (Thanks seokyun.ha and Brandon Stanley!)
- Flink: Fix LICENSE/NOTICE compliance for all versions of flink-runtime (1.20, 2.0, 2.1) (#16216) (Thanks Kevin Liu!)
- Spark: Carry over changes to LICENSE and NOTICE in older Spark versions. (#16142) (Thanks Ryan Blue!)
- Flink 2.1: Update LICENSE for 1.11. (#16102) (Thanks Ryan Blue!)
- Flink: RewriteDataFile support dynamic filter (#15865) (Thanks GuoYu!)
- Flink: Apply LICENSE changes to older Flink versions. (#16159) (Thanks Ryan Blue!)
- Core: Avoid unnecessary manifest scanning during snapshot expiration incremental cleanup (#16077) (Thanks hemanthboyina!)
- OpenAPI, Core: Disambiguate the intent of REFS snapshot mode (#16252) (Thanks gaborkaszab and Eduard Tudenhoefner!)
- Core: Fix RejectedExecutionException in InMemoryLockManager when multiple catalogs share default lock manager (#15862) (Thanks Manu Zhang!)
- Spark 3.4: Set data file sort_order_id in manifest for writes from Spark (#16308) (Thanks Kevin Liu!)
- API, Core: Handle 404 from /v1/config for missing warehouses (#16059) (Thanks Oguzhan Unlu!)
- Parquet: Add write.parquet.page-version table property (#15700) (Thanks Harrison Crosse!)
- Spark: backport PR #15512 to v3.4, v3.5, v4.0 for WAP branch delete fix (#16245) (Thanks Steven Zhen Wu and Claude Opus 4.7 (1M context)!)
- API: Implement notStartsWith bounds check in StrictMetricsEvaluator (#15883) (Thanks Bharath Krishna!)
- Fix for vectorized builder variant handling (#16087) (Thanks Neelesh Salian!)
- Core: Use Idiomatic ThreadLocal cleanup in CommitMetadata (#15284) (#16031) (Thanks Anupam Yadav!)
- GCP: Fix LICENSE, NOTICE, and runtime-deps for gcp-bundle (#16182) (Thanks Kevin Liu!)
- REST Spec: Clarify identifier uniqueness across tables and views (#15691) (Thanks Steven Zhen Wu!)
- Azure: Fix LICENSE, NOTICE, and runtime-deps for azure-bundle (#16181) (Thanks Kevin Liu!)
- Flink: Fix watermark value which should be min timestamp minus one (#15884) (Thanks Chase Zhang!)
- AWS: Fix LICENSE/NOTICE compliance for aws-bundle (#16196) (Thanks Kevin Liu!)
- INFRA: Expand Trivy CVE scan to all bundle and runtime modules (#16291) (Thanks Kevin Liu and Copilot!)
- AWS: Fix stale LICENSE entry for Parquet, clarify failsafe attribution (#16179) (Thanks Kevin Liu and Copilot!)
- Flink: SQL: Make Dynamic sink options to be configurable in SQL (#15780) (Thanks Swapna Marru!)
- Core: Propagate server error message in failed remote scan planning responses (#16024) (Thanks Prashant Singh!)
- Add Oracle as an Iceberg vendor (#16251) (Thanks Alex Miller!)
- Spark 4.1: Update LICENSE and NOTICE for 1.11. (#16104) (Thanks Ryan Blue!)
- Core, Spark: Verify that TRUNCATE removes orphaned DVs (#16078) (Thanks Eduard Tudenhoefner!)
- Core: Add test to validate we can't delete map value during schema evolution (#15767) (Thanks Mukund Thakur!)
- Core: Fix child AuthSession inheriting parent's expiresAtMillis (#15999) (Thanks Bharath Krishna!)
- Spec: Update formatting in tables to use material content tabs (#14656) (Thanks Amogh Jahagirdar, Claude Sonnet 4.6, and Kevin Liu!)
- Flink: Backport add Nanosecond Precision Support for Flink-Iceberg Integration to Flink 1.20 (#16240) (Thanks pvary!)
- AWS: remove extra/staled LICENSE entry bundled by Parquet (#16180) (Thanks Kevin Liu!)
- Spark: fix delete from branch for canDeleteWhere where it does not resolve to the correct branch (#15512) (Thanks Yingjian Wu!)
- Data: Add TCK tests for Schema Evolution  in BaseFormatModelTests (#15843) (Thanks GuoYu!)
- Data: Add TCK tests for Metadata Columns in BaseFormatModelTests (#15675) (Thanks GuoYu!)
- Flink: Define Joda Time in libs.versions.toml file (#16191) (Thanks Talat UYARER!)
- Flink: Bundle flink-metrics-dropwizard in runtime jar (#16126) (Thanks Maximilian Michels!)
- API: Remove unnecessary EOFException in FileRange constructor. (#15973) (Thanks Mukund Thakur!)
- Flink: Backport add Nanosecond Precision Support for Flink-Iceberg Integration (#16183) (Thanks Talat UYARER!)
- Spark: Migrate RollBackStageTable to use SupportsDeleteV2 (#16211) (Thanks drexler-sky!)
- Core: Surface failed scan planning even when server omits error payload (#16197) (Thanks Prashant Singh!)
- Validate manifest sequence numbers are equal during inheritance (#16091) (Thanks Anoop Johnson!)
- Runtimes, Bundles: Add runtime-deps.txt files to track dependencies (#16081) (Thanks Kevin Liu!)
- Flink:Backport RewriteDataFile support dynamic filter (#16132) (Thanks GuoYu!)
- API: Use column bounds to evaluate startsWith in StrictMetricsEvaluator (#15902) (Thanks Bharath Krishna!)
- Core: Replace string-based schema projection with selection on field-id (#16184) (Thanks Hongyue and Steve Zhang!)
- Arrow: Align vectorized reader handling of unsigned Parquet integers with BaseParquetReaders (#16006) (Thanks drexler-sky and Evan Wu!)
- ORC: Backport add _row_id and _last_updated_sequence_number raeder in Orc to support lineage (#16256) (Thanks pvary!)
- Data: Add TCK tests for metrics collection in BaseFormatModelTests (#15906) (Thanks GuoYu!)
- Flink: Backport add Nanosecond Precision Support for Flink-Iceberg Integration to Flink 2.0 - missing changes (#16239) (Thanks pvary!)
- Spark 3.4, 3.5, 4.0: Include snapshotId and branch in SparkTable equals and hashCode (#15840) (Thanks Bharath Krishna!)
- Spark 3.4, 3.5, 4.0: Migrate SparkWriteBuilder to SupportsOverwriteV2 (#16178) (Thanks drexler-sky!)
- Move all analyticscore references behind a AnalyticsCoreUtil class (#16258) (Thanks Talat UYARER!)
- Spark 4.1: Migrate SparkCopyOnWriteScan to SupportsRuntimeV2Filtering (#16295) (Thanks drexler-sky!)
- Azure: Avoid depending on KeyWrapAlgorithm in AzureProperties (#16186) (Thanks Yuya Ebihara!)
- ORC: Fix connection leak in OrcIterable (#16086) (Thanks Denys Kuzmenko!)
- Flink: Do not ship optional flink-metrics-dropwizard dependency (#16155) (Thanks Maximilian Michels!)
- Spark 4.1: Migrate SparkWriteBuilder to SupportsOverwriteV2 (#16164) (Thanks drexler-sky!)
- Flink 2.1: Remove flink-metrics-dropwizard from runtime (#16093) (Thanks Ryan Blue!)
- Spark: Fix RoaringBitmap version in runtime-deps.txt (#16076) (Thanks Yuya Ebihara!)
- Spark 3.4: Backport Async Micro Batch Planner to 3.4 (#16311) (Thanks Kevin Liu!)
- Sink connector crashes on timestamps with fractional seconds and colon-separated UTC offset (Fixes #15838) (#15839) (Thanks Soumyajit Sahu and Som Sahu!)
- Flink: Backport: Dynamic sink options to be configurable in SQL (#16209) (Thanks Swapna Marru!)
- Site: Remove Iceberg Summit 2026 section as the event has passed (#16166) (Thanks Talat UYARER!)
- GCP Bundle: Remove JSR 305 (#16106) (Thanks Ryan Blue!)
- Core: Validate v2 deletes against concurrent format upgrade (#16146) (Thanks Hongyue and Steve Zhang!)
- Spark 4.0: Backport Aync Micro Batch Planner Feature (#15876) (Thanks Ruijing Li!)
- Spark 3.5: Backport Async Micro Batch Planner to 3.5 (#15992) (Thanks Ruijing Li!)
- Open API: Remove runtime Jar from build and deploy (#16163) (Thanks Ryan Blue!)
- Spark 4.1: Parameterize TestDeleteFrom with format-version (#16098) (Thanks Eduard Tudenhoefner!)
- AWS Bundle: Exclude logging dependencies (#16105) (Thanks Ryan Blue!)
- Flink: Backport: Bundle flink-metrics-dropwizard in runtime jar (#16141) (Thanks Maximilian Michels!)
- Flink: Backport removal of optional flink-metrics-dropwizard dependency to v2.0 and v1.20 (#16230) (Thanks Kevin Liu!)

### Suppressed Commits

- CI: Add PR title check workflow (#16101) (Thanks Manu Zhang!)
- Docs: Add missing v3 data types to status page (#16228) (Thanks Manu Zhang!)
- test: add ns1/ns2 to RCK view test namespace purge list (#16050) (Thanks M Alvee!)
- Build: Fix transitive dependency CVEs across all distributions (#16290) (Thanks Kevin Liu!)
- CI: Use specific patch versions in workflow action comments (#16229) (Thanks Kevin Liu!)
- Docs: Move catalog properties to catalog section (#15848) (Thanks gaborkaszab!)
- Build: Correct actions/labeler version comment to v6.0.1 (#16225) (Thanks Maximilian Michels!)
- Build: Improve PR title check pattern for multi-word prefixes and reverts (#16301) (Thanks Manu Zhang and Kevin Liu!)
- Docs: Update Oracle vendor description (#16261) (Thanks Alex Miller!)
- Docs: Document CATALOG_* env vars in iceberg-rest-fixture README (#16007) (Thanks Rexwell Minnis!)
- Docs: Document general REST catalog properties (#15871) (Thanks gaborkaszab!)
- Build: Check runtime deps baseline for all engine versions in CI (#16103) (Thanks Russell Spitzer!)
- Build: Bump software.amazon.awssdk:bom from 2.42.41 to 2.44.0 (#16279) (Thanks Huaxin Gao and Cursor!)
- Build: Bump software.amazon.awssdk:bom from 2.42.36 to 2.42.41 (#16206) (Thanks Yuya Ebihara and dependabot[bot]!)
- Build: Bump com.google.cloud:libraries-bom from 26.79.0 to 26.80.0 (#16152) (Thanks Yuya Ebihara and dependabot[bot]!)
- Build: Bump software.amazon.awssdk:bom from 2.42.33 to 2.42.36 (#16151) (Thanks Yuya Ebihara and dependabot[bot]!)
- Build: Bump to Parquet 1.17.1 (#16257) (Thanks Fokko Driesprong and Kevin Liu!)
- Build: Bump org.openapitools:openapi-generator-gradle-plugin from 7.21.0 to 7.22.0 (#16278) (Thanks Huaxin Gao and Cursor!)
- Build: Bump io.grpc:grpc-netty-shaded from 1.80.0 to 1.81.0 (#16277) (Thanks Huaxin Gao and Cursor!)
- Build: Bump junit from 5.14.3 to 5.14.4 (#16271) (Thanks dependabot[bot]!)
- Build: Bump github/codeql-action from 4.35.2 to 4.35.3 (#16275) (Thanks dependabot[bot]!)
- Build: Bump junit-platform from 1.14.3 to 1.14.4 (#16272) (Thanks dependabot[bot]!)
- Build: Bump joda-time:joda-time from 2.5 to 2.14.2 (#16270) (Thanks dependabot[bot]!)
- Build: Bump jackson-bom from 2.21.2 to 2.21.3 (#16269) (Thanks dependabot[bot]!)
- Build: Bump org.apache.httpcomponents.client5:httpclient5 (#16204) (Thanks dependabot[bot]!)
- Build: Bump nessie from 0.107.4 to 0.107.5 (#16202) (Thanks dependabot[bot]!)
- Build: Bump testcontainers from 2.0.4 to 2.0.5 (#16201) (Thanks dependabot[bot]!)
- Build: Bump openapi-spec-validator from 0.8.4 to 0.8.5 (#16200) (Thanks dependabot[bot]!)
- Build: Bump datamodel-code-generator from 0.56.0 to 0.56.1 (#16114) (Thanks dependabot[bot]!)
- Build: Bump mkdocs-rss-plugin from 1.18.1 to 1.19.0 (#16113) (Thanks dependabot[bot]!)
- Build: Bump guava from 33.5.0-jre to 33.6.0-jre (#16116) (Thanks dependabot[bot]!)
- Build: Bump bouncycastle from 1.82 to 1.84 (#16117) (Thanks dependabot[bot]!)
- Build: Bump github/codeql-action from 4.35.1 to 4.35.2 (#16118) (Thanks dependabot[bot]!)
- Build: Bump org.xerial:sqlite-jdbc from 3.51.3.0 to 3.53.0.0 (#16120) (Thanks dependabot[bot]!)
- Build: Bump astral-sh/setup-uv from 8.0.0 to 8.1.0 (#16121) (Thanks dependabot[bot]!)
- Build: Bump zizmorcore/zizmor-action from 0.5.2 to 0.5.3 (#16122) (Thanks dependabot[bot]!)

## apache/iceberg-python

### Python

_Top 16 themes from 51 scored commits._

- Top themes: `16`
- Commits covered by top themes: `17`
- Other reviewable commits: `0`
- Suppressed commits: `34`

- Catalog views: add and expand view support (#3224, #3288) (Thanks Yuya Ebihara and spr0els!)
- Add support for 'overwrite' option in register_table (#3290) (Thanks Yuya Ebihara!)
- infra: add python 3.14 support (#3299) (Thanks Adam and Kevin Liu!)
- Fix DELETED manifest entry snapshot_id in OverwriteFiles (#3237) (Thanks Sotaro Hikita!)
- perf: Hoist `table_metadata` at remaining repeat-access (#3301) (Thanks Ruiyang Wang!)
- bug: NoopCatalog should return False, not throw error (#3284) (Thanks Alex Stephen!)
- Update NOTICE year 2025 -> 2026 (#3332) (Thanks Kevin Liu!)
- Document `TableAlreadyExistsError` in `rename_table` (#3289) (Thanks Yuya Ebihara!)
- fix:update config during table refresh (#3327) (Thanks Yingjian Wu!)
- Fix deepcopy for `And`, `Or`, and `Not` expressions (#3295) (Thanks Rob Reeves!)
- Reading upper/lower bounds values with type promotions (#3293) (Thanks Alex Stephen!)
- Remove unused code (#3326) (Thanks Yuya Ebihara!)
- fix(tests): isolate state in `test_write_optional_list` (#3334) (Thanks Paul Mathew!)
- perf: build partition filter with balanced tree to avoid RecursionError (#3264) (Thanks Yingjian Wu!)
- fix: SaslServer busy-loop causes process hang after test suite (#3305) (Thanks Kevin Liu!)
- Initial work for file format writer API (#3119) (Thanks Neelesh Salian!)

### Suppressed Commits

- CI: Use specific patch versions in workflow action comments (#3331) (Thanks Kevin Liu!)
- Bump daft dependency to >=0.7.10 (fix Python 3.14 compatibility) (#3323) (Thanks Kevin Liu!)
- Build: Bump fastavro from 1.12.1 to 1.12.2 (#3310) (Thanks dependabot[bot]!)
- Build: Bump rich from 14.3.3 to 15.0.0 (#3283) (Thanks dependabot[bot]!)
- Build: Bump mkdocstrings from 1.0.3 to 1.0.4 (#3282) (Thanks dependabot[bot]!)
- Build: Bump mkdocs-section-index from 0.3.11 to 0.3.12 (#3276) (Thanks dependabot[bot]!)
- Build: Bump pydantic from 2.13.2 to 2.13.3 (#3314) (Thanks dependabot[bot]!)
- Build: Bump pydantic from 2.12.5 to 2.13.2 (#3275) (Thanks dependabot[bot]!)
- Build: Bump mypy-boto3-dynamodb from 1.42.73 to 1.43.0 (#3345) (Thanks dependabot[bot]!)
- Build: Bump cachetools from 7.0.6 to 7.1.0 (#3344) (Thanks dependabot[bot]!)
- Build: Bump google-auth from 2.49.2 to 2.50.0 (#3343) (Thanks dependabot[bot]!)
- Build: Bump mypy-boto3-glue from 1.42.89 to 1.43.0 (#3342) (Thanks dependabot[bot]!)
- Build: Bump prek from 0.3.10 to 0.3.11 (#3341) (Thanks dependabot[bot]!)
- Build: Bump huggingface-hub from 1.12.0 to 1.13.0 (#3340) (Thanks dependabot[bot]!)
- Build: Bump github/codeql-action from 4.35.2 to 4.35.3 (#3339) (Thanks dependabot[bot]!)
- Build: Bump mistune from 3.2.0 to 3.2.1 (#3333) (Thanks dependabot[bot]!)
- Build: Bump jupyter-server from 2.17.0 to 2.18.0 (#3329) (Thanks dependabot[bot]!)
- Build: Bump zizmorcore/zizmor-action from 0.5.2 to 0.5.3 (#3273) (Thanks dependabot[bot]!)
- Build: Bump polars from 1.39.3 to 1.40.1 (#3306) (Thanks dependabot[bot]!)
- Build: Bump cachetools from 7.0.5 to 7.0.6 (#3307) (Thanks dependabot[bot]!)
- Build: Bump psycopg2-binary from 2.9.11 to 2.9.12 (#3308) (Thanks dependabot[bot]!)
- Build: Bump huggingface-hub from 1.11.0 to 1.12.0 (#3309) (Thanks dependabot[bot]!)
- Build: Bump s3fs from 2026.2.0 to 2026.3.0 (#3311) (Thanks dependabot[bot]!)
- Build: Bump pyroaring from 1.0.4 to 1.1.0 (#3312) (Thanks dependabot[bot]!)
- Build: Bump click from 8.3.2 to 8.3.3 (#3315) (Thanks dependabot[bot]!)
- Build: Bump prek from 0.3.9 to 0.3.10 (#3316) (Thanks dependabot[bot]!)
- Build: Bump boto3 from 1.42.91 to 1.42.96 (#3317) (Thanks dependabot[bot]!)
- Build: Bump jupyterlab from 4.5.6 to 4.5.7 (#3300) (Thanks dependabot[bot]!)
- Build: Bump prek from 0.3.8 to 0.3.9 (#3281) (Thanks dependabot[bot]!)
- Build: Bump mypy-boto3-glue from 1.42.70 to 1.42.89 (#3280) (Thanks dependabot[bot]!)
- Build: Bump huggingface-hub from 1.10.1 to 1.11.0 (#3279) (Thanks dependabot[bot]!)
- Build: Bump duckdb from 1.5.1 to 1.5.2 (#3278) (Thanks dependabot[bot]!)
- Build: Bump daft from 0.6.14 to 0.7.9 (#3277) (Thanks dependabot[bot]!)
- Build: Bump boto3 from 1.42.84 to 1.42.91 (#3274) (Thanks dependabot[bot]!)

## apache/iceberg-rust

### Rust

_Top 14 themes from 37 scored commits._

- Top themes: `14`
- Commits covered by top themes: `15`
- Other reviewable commits: `0`
- Suppressed commits: `22`

- feat(reader): Add read_with_metrics() for scan I/O metrics (#2349) (Thanks Matt Butrovich, Claude Opus 4.6 (1M context), and blackmwk!)
- Encryption: add key management and encrypted IO support (#2339, #2340) (Thanks Xander and Claude Opus 4.6 (1M context)!)
- fix(catalog/memory): relax strict ms inequality in test_update_table (#2395) (Thanks Kurtis Wright!)
- feat(schema): Add `update_schema` action to enable table schema updates (#2120) (Thanks Victor Ghita and Claude Sonnet 4.6!)
- fix(sqllogictest): add missing tokio `rt-multi-thread` feature (#2386) (Thanks Charles-Antoine Leger!)
- fix: allow missing sequence-number in v2 snapshots for v1-upgraded tables (#2127) (Thanks Jem Bishop!)
- feat(datatypes): add optional and required constructors for MapType (#2405) (Thanks Liang Gong!)
- fix: NaN pushdown correctly pushes down NaNs correctness issue  (#2351) (Thanks Xander!)
- Split arrow reader into smaller modules (#2358) (Thanks blackmwk and Claude Opus 4.7 (1M context)!)
- Fix RUSTSEC-2026-0122 (#2437) (Thanks blackmwk!)
- fix(transaction): fix previous snapshot summary fetching (#2391) (Thanks dentiny!)
- feat(datafusion): show pushed-down limit in IcebergTableScan EXPLAIN output (#2360) (Thanks Charles-Antoine Leger!)
- chore: Improve release process (#2381) (Thanks Shawn Chang!)
- fix(tests): remove unnecessary `.to_string()` calls for metadata_location (#2407) (Thanks Liang Gong!)

### Suppressed Commits

- ci(python): verify wheel abi3 compatibility with --no-build (#2388) (Thanks Kevin Liu!)
- CI: Use specific patch versions in workflow action comments (#2412) (Thanks Kevin Liu!)
- docs: Correct docs for Int128 and UInt128 being big-endian not little-endian (#2397) (Thanks Xander!)
- docs(arrow): clarify ScanMetrics::bytes_read includes delete files (#2379) (Thanks Matt Butrovich!)
- docs: bump version for python binding (#2377) (Thanks Kevin Liu!)
- chore(deps): bump opendal to 0.56, migrate to reqsign-core 3.0 (#2401) (Thanks Krisztián Szűcs!)
- fix: Bump rustls-webpki from 0.103.12 to 0.103.13 to fix RUSTSEC-2026-0104 (#2356) (Thanks Shawn Chang!)
- chore(deps): Bump crate-ci/typos from 1.45.1 to 1.46.0 (#2424) (Thanks dependabot[bot]!)
- chore(deps): Bump taiki-e/install-action from 2.75.22 to 2.75.30 (#2425) (Thanks dependabot[bot]!)
- chore(deps): Bump github/codeql-action from 4.35.2 to 4.35.3 (#2426) (Thanks dependabot[bot]!)
- chore(deps): Bump the arrow-parquet group with 6 updates (#2427) (Thanks dependabot[bot] and blackmwk!)
- chore(deps): Bump serde_with from 3.18.0 to 3.19.0 (#2428) (Thanks dependabot[bot]!)
- chore(deps): Bump reqwest from 0.12.28 to 0.13.3 (#2429) (Thanks dependabot[bot]!)
- chore(deps): Bump taiki-e/install-action from 2.75.18 to 2.75.22 (#2400) (Thanks dependabot[bot]!)
- chore(deps): Bump aws-sdk-glue from 1.142.0 to 1.142.1 (#2399) (Thanks dependabot[bot]!)
- chore(deps): Bump zizmorcore/zizmor-action from 0.5.2 to 0.5.3 (#2368) (Thanks dependabot[bot] and blackmwk!)
- chore(deps): Bump taiki-e/install-action from 2.75.7 to 2.75.18 (#2370) (Thanks dependabot[bot]!)
- chore(deps): Bump astral-sh/setup-uv from 8.0.0 to 8.1.0 (#2371) (Thanks dependabot[bot]!)
- chore(deps): Bump crate-ci/typos from 1.45.0 to 1.45.1 (#2372) (Thanks dependabot[bot]!)
- chore(deps): Bump tokio from 1.51.1 to 1.52.1 (#2374) (Thanks dependabot[bot]!)
- chore(deps): Bump datafusion-sqllogictest from 53.0.0 to 53.1.0 (#2369) (Thanks dependabot[bot]!)
- chore(deps): Bump datafusion-cli from 53.0.0 to 53.1.0 (#2373) (Thanks dependabot[bot]!)

## apache/iceberg-go

### Go

_Top 20 themes from 65 scored commits._

- Top themes: `20`
- Commits covered by top themes: `25`
- Other reviewable commits: `27`
- Suppressed commits: `13`

- Compaction and rewrite data files: expand rewrite planning and execution (#928, #934, #947, #948, #1033) (Thanks Tobias Pütz and Andrei Tserakhau!)
- feat(io): add BulkRemovableIO interface(#914) (#916) (Thanks Tanmay Rauth!)
- Deletion vectors: add read, write, and validation support (#866, #1041) (Thanks Andrei Tserakhau and Shreyas Mishra!)
- feat(catalog): add version-hint management for Hadoop catalog (Thanks Tanmay Rauth!)
- feat(cli): add maintenance command wiring and stubs (#1073) (Thanks Tanmay Rauth!)
- fix(manifest): allow ManifestListWriter to reference lower-version manifests (#1030) (Thanks Ashley Jeffs!)
- feat(io): add ListableIO interface to replace reflect-based directory walking (#913) (#917) (Thanks Tanmay Rauth!)
- fix(occ): manifest list rebuild (#982) (Thanks Masa and masa hoashi!)
- fix(manifest): restore data_file.distinct_counts on v1/v2 Avro schemas (#1044) (Thanks Masa!)
- feat(catalog): add hadoop namespace operations (#963) (Thanks Tanmay Rauth!)
- feat(catalog): add Hadoop catalog scaffold with path helpers (#953) (Thanks Tanmay Rauth!)
- feat(config,cmd/iceberg): support more rest options in config (#933) (Thanks Matt Topol!)
- feat(cli): add partition-stats command (#1065) (Thanks Tanmay Rauth!)
- feat(table): support zstd metadata compression codec (#1020) (Thanks Tanmay Rauth!)
- feat(io): add native in-memory FS (#1025) (Thanks Alessandro Nori!)
- fix(io): resolve S3 PermanentRedirect for S3 Table Buckets (#974) (#975) (Thanks Tanmay Rauth!)
- feat(manifest): omit data_file.distinct_counts on v3 manifests (#1039) (Thanks Masa!)
- feat(catalog): hadoop table and namespace CRUD operations (#969) (Thanks Tanmay Rauth!)
- feat(catalog): hadoop cli integration (#1034) (Thanks Tanmay Rauth!)
- fix(occ): RowDelta uses partition-scoped conflict check instead of AlwaysTrue (#983) (Thanks Masa!)

### Other Reviewable Commits

- feat(table): skip validator registration for no-op producers (#1022) (Thanks Hectar!)
- feat(manifest)!: Replace FetchEntries with iterator approach (#985) (Thanks Artem Alperin!)
- feat(table): add SetPartitionStatisticsUpdate and RemovePartitionStatisticsUpdate (#1018) (Thanks Tanmay Rauth!)
- feat(catalog): hadoop list drop rename operations (#970) (Thanks Tanmay Rauth!)
- fix(table): seed UpdateSchema id counter from metadata LastColumnID (#936) (Thanks Ashley Jeffs!)
- feat(table/dv): plumb cardinality validation through ReadDV (#1056) (Thanks Andrei Tserakhau!)
- feat(table): refresh-and-replay between commit retries (#945) (Thanks Andrei Tserakhau!)
- fix: data races in exprEvaluator.Eval and manifestEvalVisitor.Eval (#954) (Thanks Varun Venkatesh!)
- feat(table): warn when writing Parquet position-deletes on v3 (#1040) (Thanks Andrei Tserakhau!)
- feat(catalog): wrap concurrent-write conflicts with ErrCommitFailed (#944) (Thanks Andrei Tserakhau!)
- fix(table): include expected vs found snapshot id in AssertRefSnapshotID errors (#940) (#952) (Thanks Tanmay Rauth!)
- feat(cli): add info command for single-screen table summary (#1064) (Thanks Tanmay Rauth!)
- feat(manifest): Add tests for Entries and migrate snapshotProducer (#1031) (Thanks Artem Alperin!)
- feat(cli): add --schema-from-file flag to infer table schema from parquet files (#927) (Thanks Tanmay Rauth!)
- refactor(cli): migrate from docopt-go to go-arg (#965) (#980) (Thanks Tanmay Rauth!)
- fix(schema): data race in MarshalJSON on shared *Schema (#967) (Thanks Tanmay Rauth!)
- fix: use floored division in HourTransform for pre-epoch timestamps (#924) (#926) (Thanks Tanmay Rauth!)
- fix(table): treat empty-base conflict context as fully concurrent (#979) (Thanks Andrei Tserakhau!)
- fix(table): use Abort() on error path to prevent panic in stream() (#962) (Thanks Tanmay Rauth!)
- fix(rest): making non 200 rest errors more informative (#972) (Thanks David D Zhao!)
- fix(table): remove double Release() on struct array in ToRequestedSchema (#956) (Thanks Tanmay Rauth!)
- feat(table): port remaining v3 metadata-upgrade validation rules (#1070) (Thanks Tanmay Rauth!)
- feat(io): Better error message for unregistered IO scheme (#960) (Thanks David D Zhao!)
- feat(schema): reject complex type defaults #1011  (#1017) (Thanks Tanmay Rauth!)
- feat(arrow): map unknown type to null (#1035) (Thanks TT!)
- feat: added override of http client as well as readme on utils.WithAw… (#981) (Thanks Ankit Sharma!)
- feat(test): add Spark integration test infrastructure for Hadoop catalog (#968) (Thanks Tanmay Rauth!)

### Suppressed Commits

- test(table): add v3 OCC row lineage regression tests (#998) (#1043) (Thanks Tanmay Rauth!)
- test(table): add round-trip test for v3 metadata with partition-statistics (#1012) (#1019) (Thanks Tanmay Rauth!)
- test(table): add regression test for UpdateSchema id counter seeding (#942) (#951) (Thanks Tanmay Rauth!)
- fix(ci): correct labeler action version tag (#1026) (Thanks Alessandro Nori!)
- CI: Use specific patch versions in workflow action comments (#1032) (Thanks Kevin Liu!)
- build(deps): bump arrow-go to v18.6.0 and substrait-go to v8.1.0 (#949) (Thanks Ben Bellick!)
- build(deps): bump github.com/apache/thrift from 0.22.0 to 0.23.0 (#1036) (Thanks dependabot[bot]!)
- build(deps): bump github.com/in-toto/in-toto-golang from 0.10.0 to 0.11.0 (#1042) (Thanks dependabot[bot]!)
- build(deps): bump the gomod_updates group across 1 directory with 10 updates (#1047) (Thanks dependabot[bot]!)
- build(deps): bump the gomod_updates group with 7 updates (#939) (Thanks dependabot[bot]!)
- build(deps): bump github/codeql-action from 4.35.2 to 4.35.3 (#1046) (Thanks dependabot[bot]!)
- build(deps): bump github/codeql-action from 4.35.1 to 4.35.2 (#938) (Thanks dependabot[bot]!)
- build(deps): bump zizmorcore/zizmor-action from 0.5.2 to 0.5.3 (#937) (Thanks dependabot[bot]!)

## apache/iceberg-cpp

### C++

_Top 9 themes from 19 scored commits._

- Top themes: `9`
- Commits covered by top themes: `9`
- Other reviewable commits: `0`
- Suppressed commits: `10`

- feat(io): add streaming FileIO support (#641) (Thanks Gang Wu!)
- feat: add iceberg_data library alongside iceberg (#631) (Thanks Junwang Zhao!)
- feat(data): add delete filter support (#650) (Thanks Gang Wu!)
- feat: add ReachableFileCleanup to expire snapshots (#592) (Thanks Xinli Shang!)
- feat: retry failed transaction commit (#626) (Thanks SkylerLin!)
- fix: concurrent Lazy::Get should get correct result (#634) (Thanks Zehua Zou!)
- fix: repair shared package linkage and export scan builder symbols (#635) (Thanks Junwang Zhao!)
- refactor(util): make retry policy explicit and deterministic (#633) (Thanks Gang Wu!)
- fix(cmake): use consistent generator expressions to link libraries (#639) (Thanks Junwang Zhao!)

### Suppressed Commits

- fix: typo in RoaringPositionBitmap deletion vector note (#632) (Thanks Junwang Zhao!)
- CI: Use specific patch versions in workflow action comments (#644) (Thanks Kevin Liu!)
- ci: split S3/MinIO into a Linux and macOS-only workflow (#642) (Thanks Junwang Zhao!)
- fix(ci): restore auth for docs gh-pages deploy (#625) (Thanks Gang Wu and Kevin Liu!)
- ci: use ilammy/msvc-dev-cmd for Windows MSVC environment (#643) (Thanks Junwang Zhao!)
- chore: bump arrow-cpp to 24.0.0 (#623) (Thanks Gang Wu!)
- chore(deps): bump github/codeql-action from 4.35.2 to 4.35.3 (#647) (Thanks dependabot[bot]!)
- chore(deps): bump mozilla-actions/sccache-action from 0.0.9 to 0.0.10 (#636) (Thanks dependabot[bot]!)
- chore(deps): bump zizmorcore/zizmor-action from 0.5.2 to 0.5.3 (#630) (Thanks dependabot[bot]!)
- chore(deps): bump github/codeql-action from 4.35.1 to 4.35.2 (#629) (Thanks dependabot[bot]!)
