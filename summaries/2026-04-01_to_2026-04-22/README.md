# Iceberg Community Sync Summary

- Period: `2026-04-01` to before `2026-04-22`
- Review candidates: `186`

## apache/iceberg

### Java

_Top 20 themes from 71 scored commits._

- Top themes: `20`
- Commits covered by top themes: `20`
- Other reviewable commits: `16`
- Suppressed commits: `35`

- Core: Add fromId to EntryStatus and ManifestEntry.Status (#15983) (Thanks Anoop Johnson!)
- Core: Introduce default values in RESTCatalogProperties (#15873) (Thanks gaborkaszab!)
- Flink: Add passthroughRecords option to DynamicIcebergSink (#15433) (Thanks Han You and Jordan Epstein!)
- Core, API, Spark: Add FileContent.fromId (#15953) (Thanks Anoop Johnson!)
- Core: Expose HostnameVerificationPolicy in TLSConfigurer (#15500) (Thanks Alexandre Dutra!)
- Spec: Add 404 response for config endpoint (#15746) (Thanks Oguzhan Unlu!)
- Spark (4.0, 3.5): Set data file sort_order_id in manifest for writes from Spark (#15832) (Thanks jbewing!)
- AWS: Add chunked encoding configuration for S3 requests (#15242) (Thanks Jiajia Li!)
- API, Core: Move stats classes to core as package-private (#15971) (Thanks Eduard Tudenhoefner!)
- Parquet: Fix NPE in ParquetAvroWriter when schema contains variant type (#15934) (Thanks Neelesh Salian!)
- Core: Expose MetricsConfig.from method with 3-parameter version (#15819) (Thanks Yuya Ebihara!)
- API: Relax partition name check when source column is dropped (#15967) (Thanks Russell Spitzer!)
- AWS: Add proxy system property and environment variable configuration for HTTP clients (#15506) (Thanks Mervyn Lobo!)
- API: Fix TableIdentifier.toLowerCase to use Locale.ROOT for namespace levels (#15956) (#15958) (Thanks Govindarajan!)
- Flink: Fix checkArgument message for flink streaming (#15907) (Thanks genxiong7!)
- Core: Fix StructLikeWrapper.equals exception with mismatched partition types (#15945) (Thanks Yuya Ebihara!)
- Hive encryption nits (#14659) (Thanks Sreesh Maheshwar and Claude Opus 4.6 (1M context)!)
- AWS, Core: Switch Jetty to use new Compression API for GZIP (#15043) (Thanks Eduard Tudenhoefner!)
- Flink 2.1: Fix forward-writer chaining regression in DynamicIcebergSink (#16026) (Thanks drexler-sky!)
- API: Fix FileRange validation to reject negative offset/length (#15926) (Thanks Barry!)

### Other Reviewable Commits

- Core : Make REST scan planning poll timeout configurable (#15863) (Thanks Rahul Shivu Mahadev!)
- Flink: Set generator parallelism to match input in DynamicIcebergSink (#15849) (Thanks Sachin Ranjalkar!)
- AWS: Close custom AwsCredentialsProvider in RESTSigV4AuthSession (#15818) (Thanks Rulin Xing!)
- Flink: Backport add passthroughRecords option to DynamicIcebergSink (#16019) (Thanks Han You!)
- Core: Use Stream overload for reading response in HTTPClient (#15648) (Thanks alpbeysir!)
- Spark: Replace deprecated registerTempTable with createOrReplaceTempView (#16063) (Thanks drexler-sky!)
- Core: Optimize RoaringPositionBitmap.setRange with native range API (#15791) (Thanks Sebastian Baunsgaard!)
- API: Include size unit in avg/max value size fields (#15939) (Thanks Eduard Tudenhoefner!)
- Core: Upgrade Jetty to 12.1.5 (#10837) (Thanks Eduard Tudenhoefner and manuzhang!)
- Kafka Connect: Fix source offset tracking when SMTs modify the record topic (#15880) (Thanks kumarpritam863 and Pritam Kumar Mishra!)
- Spark 4.1: Add runtime-deps.txt. (#15860) (Thanks Ryan Blue!)
- Kafka Connect: Do not fail if no partitions assigned (#15955) (Thanks kumarpritam863, Pritam Kumar Mishra, and Copilot!)
- ADLS: Throw NotFoundException for inexistent input file (#15806) (Thanks Marius Grama!)
- Data: Clean engineProjection in  BaseFormatModelTests (#15995) (Thanks GuoYu!)
- Fix typos in javadoc/comment: 'intialize', 'seperated' (#15978) (Thanks Mukunda Rao Katta and MukundaKatta!)
- Update Rust status on the site (#15709) (Thanks Shawn Chang!)

### Suppressed Commits

- Add .factorypath to .gitignore (#16067) (Thanks Yuming Wang!)
- Docs: Add Apache Hive 4.2 to website (#15998) (Thanks Shohei Okumiya!)
- Docs: Add Hive Metastore schema validation warnings for schema evolution with Hive catalog (#15814) (Thanks jackylee, Copilot, and Manu Zhang!)
- Build: Fix codeql-action version comment to match pinned SHA (#15985) (Thanks Robin Moffatt!)
- Docs: Add Sail to integration and vendor (#15920) (Thanks XL Liang!)
- pass dockerhub token the safely (#15940) (Thanks Dhruv Arya!)
- Update documentation on Spark migrate procedure (#15874) (Thanks Wing Yew Poon!)
- ci: remove zizmor ignore for allowlist-check, pin to main (#15987) (Thanks Kevin Liu!)
- Build: Fix zizmor and Spark 4.1 runtime-deps CI failures (#15937) (Thanks Huaxin Gao and Neelesh Salian!)
- Docs: Fix missing semicolons in Java API Quickstart imports (#15864) (Thanks Atsuo Yamaguchi!)
- Build: Ban toLowerCase/toUpperCase without locale (#15960) (Thanks Yuya Ebihara!)
- Build: set zizmor min-severity and min-confidence to medium (#16001) (Thanks Kevin Liu!)
- Docs: Sync Go implementation status with iceberg-go (#16021) (Thanks Tanmay Rauth!)
- Build: Ignore `.githooks` (#15909) (Thanks Manu Zhang!)
- Docs: Replace deprecated 'compile' with 'implementation' in Gradle snippet (#15921) (Thanks yadavay-amzn and Anupam Yadav!)
- Docs: Document that positionDeleteWriteBuilder is for format-version 2 tables only (#15980) (Thanks sanshi!)
- Revert "Build: bump shadow-gradle-plugin to 9.4.1 (#15835)" (#15941) (Thanks Eduard Tudenhoefner!)
- Build: bump shadow-gradle-plugin to 9.4.1 (#15835) (Thanks Maksim Konstantinov!)
- Build: Bump software.amazon.awssdk:bom from 2.42.28 to 2.42.33 (#16040) (Thanks dependabot[bot]!)
- Build: Bump org.roaringbitmap:RoaringBitmap from 1.6.13 to 1.6.14 (#16042) (Thanks dependabot[bot]!)
- Build: Bump docker/build-push-action from 7.0.0 to 7.1.0 (#16041) (Thanks dependabot[bot]!)
- Build: Bump com.google.errorprone:error_prone_annotations (#16039) (Thanks dependabot[bot]!)
- Build: Bump at.yawk.lz4:lz4-java from 1.10.4 to 1.11.0 (#16038) (Thanks dependabot[bot]!)
- Build: Bump com.azure:azure-sdk-bom from 1.3.5 to 1.3.6 (#16037) (Thanks dependabot[bot]!)
- Build: Bump mkdocs-rss-plugin from 1.17.9 to 1.18.1 (#16036) (Thanks dependabot[bot]!)
- Build: Bump software.amazon.awssdk:bom from 2.42.23 to 2.42.28 (#15952) (Thanks dependabot[bot]!)
- Build: Bump jetty from 12.1.7 to 12.1.8 (#15951) (Thanks dependabot[bot]!)
- Build: Bump datamodel-code-generator from 0.55.0 to 0.56.0 (#15949) (Thanks dependabot[bot]!)
- Build: Bump io.netty:netty-buffer from 4.2.10.Final to 4.2.12.Final (#15891) (Thanks dependabot[bot]!)
- Build: Bump jetty from 12.1.5 to 12.1.7 (#15887) (Thanks dependabot[bot]!)
- Build: Bump software.amazon.awssdk:bom from 2.42.18 to 2.42.23 (#15890) (Thanks dependabot[bot]!)
- Build: Bump com.google.cloud:libraries-bom from 26.78.0 to 26.79.0 (#15889) (Thanks dependabot[bot]!)
- Build: Bump org.openapitools:openapi-generator-gradle-plugin (#15886) (Thanks dependabot[bot]!)
- Build: Bump astral-sh/setup-uv from 7.6.0 to 8.0.0 (#15888) (Thanks dependabot[bot]!)
- Build: Bump mkdocs-redirects from 1.2.2 to 1.2.3 (#15885) (Thanks dependabot[bot]!)

## apache/iceberg-python

### Python

_Top 3 themes from 24 scored commits._

- Top themes: `3`
- Commits covered by top themes: `3`
- Other reviewable commits: `0`
- Suppressed commits: `21`

- Fix ManifestEntry.snapshot_id setter writing to wrong index (#3257) (Thanks Sotaro Hikita!)
- fix: Handle optional properties in load namespace properties response (#3169) (Thanks geruh!)
- Fix pa.Schema type annotations in schema_to_pyarrow (#3261) (Thanks David Zhao!)

### Suppressed Commits

- fix zizmor ci issue by bumping codeql-action to v4.35.2 (#3245) (Thanks geruh!)
- ci: fix zizmor workflow (#3243) (Thanks Kevin Liu!)
- CI: Lock REST Fixture to 1.10.1 (#3240) (Thanks Fokko Driesprong!)
- Build: Bump pytest from 9.0.2 to 9.0.3 (#3238) (Thanks dependabot[bot]!)
- Build: Bump nbconvert from 7.17.0 to 7.17.1 (#3262) (Thanks dependabot[bot]!)
- Build: Bump boto3 from 1.40.61 to 1.42.84 (#3226) (Thanks dependabot[bot]!)
- Build: Bump bodo from 2026.2 to 2026.4 (#3253) (Thanks dependabot[bot]!)
- Build: Bump adlfs from 2026.2.0 to 2026.4.0 (#3252) (Thanks dependabot[bot]!)
- Build: Bump s3fs from 2026.2.0 to 2026.3.0 (#3251) (Thanks dependabot[bot]!)
- Build: Bump google-auth from 2.49.1 to 2.49.2 (#3250) (Thanks dependabot[bot]!)
- Build: Bump huggingface-hub from 1.9.2 to 1.10.1 (#3249) (Thanks dependabot[bot]!)
- Build: Bump requests from 2.33.0 to 2.33.1 (#3227) (Thanks dependabot[bot]!)
- Build: Bump google-cloud-bigquery from 3.40.1 to 3.41.0 (#3228) (Thanks dependabot[bot]!)
- Build: Bump huggingface-hub from 1.8.0 to 1.9.0 (#3229) (Thanks dependabot[bot]!)
- Build: Bump sqlalchemy from 2.0.48 to 2.0.49 (#3230) (Thanks dependabot[bot]!)
- Build: Bump click from 8.3.1 to 8.3.2 (#3231) (Thanks dependabot[bot]!)
- Build: Bump daft from 0.6.14 to 0.7.7 (#3232) (Thanks dependabot[bot]!)
- Build: Bump cryptography from 46.0.6 to 46.0.7 (#3223) (Thanks dependabot[bot]!)
- Build: Bump pypa/cibuildwheel from 3.4.0 to 3.4.1 (#3225) (Thanks dependabot[bot]!)
- Build: Bump s3fs from 2026.2.0 to 2026.3.0 (#3217) (Thanks dependabot[bot]!)
- Build: Bump gcsfs from 2026.2.0 to 2026.3.0 (#3218) (Thanks dependabot[bot]!)

## apache/iceberg-rust

### Rust

_Top 8 themes from 23 scored commits._

- Top themes: `8`
- Commits covered by top themes: `8`
- Other reviewable commits: `0`
- Suppressed commits: `15`

- feat(encryption) [2/N] Support encryption: Add streaming encryption/decryption (#2286) (Thanks Xander!)
- fix(storage/s3): default to virtual-host-style addressing (#2330) (Thanks Jiajia Li!)
- fix: build_fallback_field_id_map produces incorrect column indices for schemas with nested types (#2307) (Thanks Matt Butrovich and blackmwk!)
- fix: incorrect Parquet INT96 timestamp values from ArrowReader (#2301) (Thanks Matt Butrovich!)
- fix(s3tables): use 's3' as the default scheme (#2313) (Thanks R. Conner Howell!)
- refactor(storage): remove the configured_scheme parameter from storage impls (#2338) (Thanks R. Conner Howell!)
- support fixedbinary(n) (#2348) (Thanks jeff-sqds!)
- Fix RUSTSEC-2026-0097 (#2331) (Thanks blackmwk!)

### Suppressed Commits

- tests(s3tables): add s3tables end-to-end test to verify table creation/loading plus reading/writing (#2315) (Thanks Daniel Carl Jones!)
- chore: update comment tag to match the exact version to fix zizmor (#2333) (Thanks Shawn Chang!)
- Fix zizmor workflow (#2324) (Thanks blackmwk!)
- ci: fix zizmor workflow (#2334) (Thanks Kevin Liu!)
- Fix ci workflow failure (#2325) (Thanks blackmwk!)
- chore: bump datafusion to 53.1.0 (#2350) (Thanks Xander!)
- chore(deps): Bump rustls-webpki from 0.103.10 to 0.103.12 in /bindings/python (#2352) (Thanks dependabot[bot]!)
- chore(deps): Bump actions/upload-artifact from 7.0.0 to 7.0.1 (#2345) (Thanks dependabot[bot]!)
- chore(deps): Bump PyO3/maturin-action from 1.50.1 to 1.51.0 (#2346) (Thanks dependabot[bot]!)
- chore(deps): Bump minijinja from 2.18.0 to 2.19.0 (#2322) (Thanks dependabot[bot]!)
- chore(deps): Bump tokio from 1.50.0 to 1.51.0 (#2321) (Thanks dependabot[bot]!)
- chore(deps): Bump astral-sh/setup-uv from 7.3.1 to 8.0.0 (#2314) (Thanks dependabot[bot] and Shawn Chang!)
- chore(deps): Bump aws-sdk-s3tables from 1.53.0 to 1.54.0 (#2320) (Thanks dependabot[bot] and blackmwk!)
- chore(deps): Bump taiki-e/install-action from 2.70.0 to 2.73.0 (#2319) (Thanks dependabot[bot] and blackmwk!)
- chore(deps): Bump crate-ci/typos from 1.44.0 to 1.45.0 (#2318) (Thanks dependabot[bot] and blackmwk!)

## apache/iceberg-go

### Go

_Top 20 themes from 58 scored commits._

- Top themes: `20`
- Commits covered by top themes: `27`
- Other reviewable commits: `15`
- Suppressed commits: `16`

- Compaction and rewrite data files: expand rewrite planning and execution (#850, #851, #852, #892, #893, #901, #903) (Thanks Andrei Tserakhau and Abhi Rathod!)
- Row lineage: expand support for lineage-aware reads and writes (#735, #821) (Thanks Dao Thanh Tung and Andrei Tserakhau!)
- feat(table): classify deletion vectors in scan planning (#855) (Thanks Andrei Tserakhau!)
- feat(table): retry doCommit on commit-conflict errors (#830) (#912) (Thanks Andrei Tserakhau!)
- feat(catalog): add `WithOAuthTLSConfig` for separate OAuth server TLS (#895) (Thanks Lovro Mažgon!)
- fix(table): populate WriteTask.SortOrderID in data file writers (#875) (Thanks Ali Asghar!)
- fix(table): prune StatisticsList and PartitionStatsList in RemoveSnapshots (#873) (Thanks Ali Asghar!)
- feat(table)!: multi-arg transforms in partition and sort fields (#824) (Thanks Andrei Tserakhau!)
- feat(#492): implement SetStatistics, RemoveStatistics, AddEncryptionKey, RemoveEncryptionKey updates (#902) (Thanks Tanmay Rauth and Matt Topol!)
- fix(table): warn on row count mismatch in Overwrite (#894) (Thanks Andrei Tserakhau!)
- feat(table): add snapshot ancestry utility (#911) (Thanks Andrei Tserakhau!)
- fix(table): fast-append must inherit all parent manifests unconditionally (#869) (Thanks cassio-paesleme!)
- fix(table): delete statistics files in ExpireSnapshots PostCommit #837 (#882) (Thanks Tanmay Rauth!)
- fix: emit proper Avro fixed schema for FixedType partition columns (#845) (#881) (Thanks Tanmay Rauth!)
- fix(table): read retention table properties as defaults in ExpireSnapshots (#877) (Thanks Ali Asghar!)
- fix(rest): apply header.* additional props as HTTP headers on all requests (#921) (Thanks Ali Asghar!)
- feat(avro): replace hamba/avro with twmb/avro v1.5.0 (#871) (Thanks Travis Bischel and Claude Opus 4.6 (1M context)!)
- feat(table): support committing snapshots to branches other than main (#899) (Thanks Ali Asghar!)
- refactor(table): collapse DataFileStatistics.ToDataFile args into DataFileOpts (#888) (Thanks Ali Asghar!)
- feat(table): Add OpReplace to updateSnapshotSummaries (#853) (Thanks Dao Thanh Tung!)

### Other Reviewable Commits

- feat(table): add Transaction.UpgradeFormatVersion (#827) (Thanks Tyler Rockwood!)
- feat(table): Add statistics files to orphan cleanup referenced set (#848) (Thanks Dao Thanh Tung!)
- fix: decode pre-1.4 Java Iceberg legacy manifest list field names (#889) (#890) (Thanks Tanmay Rauth!)
- fix(deletes): change equality_ids array elements avro schema type from Long to Integer to match spec (#880) (Thanks Rohil Surana!)
- fix(table): read Parquet batch size from table properties (#849) (Thanks Kelly Navarro and gabrnavarro!)
- fix(ci): resolve flaky integration-setup (#858) (Thanks Andrei Tserakhau!)
- feat(table): bloom filter scan pruning for Parquet row groups (#834) (#891) (Thanks Tanmay Rauth!)
- perf(table): Decrease memory pressure by releasing records (#886) (Thanks Abhi Rathod!)
- Thread context.Context through deletedEntries() (#847) (Thanks TT!)
- fix: require Transform in NewSortOrder and add related tests (#859) (Thanks Narwhal-fish!)
- cmd/iceberg: fix CLI YAML config being ignored when docopt sets defaults (#898) (Thanks Ali Asghar!)
- fix: handle missing format-version in NewManifestReader for v1 manifests (#868) (Thanks Tyler Rockwood!)
- feat(table): wire bloom filter properties into Parquet writer (#878) (Thanks Ali Asghar!)
- fix(schema): reject duplicate field IDs at schema construction (#879) (Thanks Ali Asghar!)
- feat(table): strengthen orphan-cleanup stats referenced-set tests and document empty-path guard (#856) (Thanks Dao Thanh Tung!)

### Suppressed Commits

- docs(website): add generator scaffold for example-driven concept pages (#920) (Thanks Andrei Tserakhau!)
- ci: fix triage labeler (#910) (Thanks Matt Topol and Kevin Liu!)
- docs(website): add scanner, writer, and transaction API documentation (#919) (Thanks Tanmay Rauth!)
- ci: apply github workflow best practice (zizmor/codeql/asf-allowlist-check) (#904) (Thanks Kevin Liu!)
- docs(website): sync feature tables with README.md (#918) (Thanks Tanmay Rauth!)
- docs: expand CONTRIBUTING.md with issue claiming and PR guidelines (#887) (Thanks Andrei Tserakhau!)
- build(deps): bump the gomod_updates group with 4 updates (#872) (Thanks dependabot[bot]!)
- build(deps): bump actions/setup-go from 4.3.0 to 6.4.0 (#908) (Thanks dependabot[bot] and Matt Topol!)
- build(deps): bump go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp from 1.38.0 to 1.43.0 (#862) (Thanks dependabot[bot]!)
- build(deps): bump go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp from 1.41.0 to 1.43.0 (#864) (Thanks dependabot[bot]!)
- build(deps): bump the gomod_updates group with 5 updates (#854) (Thanks dependabot[bot]!)
- build(deps): bump github.com/go-jose/go-jose/v4 from 4.1.3 to 4.1.4 (#828) (Thanks dependabot[bot]!)
- build(deps): bump actions/checkout from 3.6.0 to 6.0.2 (#909) (Thanks dependabot[bot]!)
- build(deps): bump actions/download-artifact from 4.3.0 to 8.0.1 (#907) (Thanks dependabot[bot]!)
- build(deps): bump golangci/golangci-lint-action from 7.0.0 to 9.2.0 (#905) (Thanks dependabot[bot]!)
- build(deps): bump actions/upload-artifact from 4.6.2 to 7.0.0 (#906) (Thanks dependabot[bot]!)

## apache/iceberg-cpp

### C++

_Top 6 themes from 10 scored commits._

- Top themes: `6`
- Commits covered by top themes: `6`
- Other reviewable commits: `0`
- Suppressed commits: `4`

- feat: add s3 file io integration (#548) (Thanks liuxiaoyu!)
- feat(puffin): add format constants, utilities, and JSON serde (#603) (Thanks ZhaoXuan!)
- feat(data): add DeleteLoader for position and equality delete files (#610) (Thanks Gang Wu!)
- feat(rest): support namespace separator (#617) (Thanks Gang Wu!)
- feat: implement incremental changelog scan (#611) (Thanks wzhuo!)
- feat(perf): optimize AddRange in RoaringPositionBitmap (#608) (Thanks Sebastian Baunsgaard!)

### Suppressed Commits

- chore: add more ai related .gitignore (#621) (Thanks Zehua Zou!)
- ci: apply github workflow best practice (zizmor/codeql/asf-allowlist-check) (#618) (Thanks Kevin Liu!)
- ci: set zizmor min-severity and min-confidence to medium (#620) (Thanks Kevin Liu!)
- chore(deps): bump actions/upload-artifact from 7.0.0 to 7.0.1 (#622) (Thanks dependabot[bot]!)
