# Iceberg Community Sync Summary

- Period: `2026-04-22` to before `2026-05-13`
- Review candidates: `303`

## apache/iceberg

### Java

_Top 20 themes from 131 scored commits._

- Core: Add implementations of v4 TrackedFile interfaces (#15854) (Thanks Anoop Johnson!)
- Spark: Support writing shredded variant in Iceberg-Spark (#14297) (Thanks Aihua Xu and Neelesh Salian!)
- Spark: Backport support writing shredded variant in Iceberg-Spark (#16241) (Thanks pvary!)
- Core: Add builders for v4 structs (#16092) (Thanks Anoop Johnson and Eduard Tudenhoefner!)
- Core, Catalogs: Add support for unique table locations via catalog property (#12892) (Thanks Dmitriy Avseitsev!)
- Spark: Add unknown type support to Spark 3.4 and 3.5 (#16066) (Thanks Kurtis Wright!)
- Spark: backport PR #15512 to v3.4, v3.5, v4.0 for WAP branch delete fix (#16245) (Thanks Steven Zhen Wu and Claude Opus 4.7 (1M context)!)
- Spark: Fix LICENSE/NOTICE compliance for all versions of spark-runtime (v3.4, v3.5, v4.0, v4.1) (#16215) (Thanks Kevin Liu!)
- AWS, GCP: add Kryo round-trip regression test for refreshed storage credentials (#16112) (Thanks Akshay Thorat!)
- Core: Fix row ID assignment for EXISTING entry during a manifest merge (#16263) (Thanks Amogh Jahagirdar, ChengJi, and Russell Spitzer!)
- Flink: Add Nanosecond Precision Support for Flink-Iceberg Integration (#15475) (Thanks Talat UYARER!)
- Core: Add partition to TrackedFile (#16253) (Thanks Eduard Tudenhoefner!)
- Core: Fix JdbcCatalog & InMemoryCatalog to prevent dropping parent namespaces with children (#16061) (Thanks sagib-sqream!)
- Flink: Fix JdbcLockFactory to allow ClientPoolImpl connection retry (#16049) (Thanks Anupam Yadav!)
- Flink: Backport add Nanosecond Precision Support for Flink-Iceberg Integration to Flink 1.20 (#16240) (Thanks pvary!)
- Core, AWS: Adapt code to S3 signing endpoint promotion (#15451) (Thanks Alexandre Dutra!)
- Kafka Connect: Add Trivy CVE scan to CI (#15430) (#15430) (Thanks Robin Moffatt and Claude Opus 4.6!)
- Flink: Backport add Nanosecond Precision Support for Flink-Iceberg Integration (#16183) (Thanks Talat UYARER!)
- Spark, Hive: Fix snapshot procedure for tables with Variant columns (#15964) (Thanks Neelesh Salian!)
- ORC: Add _row_id and _last_updated_sequence_number raeder in Orc to support lineage (#15776) (Thanks GuoYu!)

## apache/iceberg-python

### Python

_Top 20 themes from 51 scored commits._

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
- CI: Use specific patch versions in workflow action comments (#3331) (Thanks Kevin Liu!)
- Remove unused code (#3326) (Thanks Yuya Ebihara!)
- fix(tests): isolate state in `test_write_optional_list` (#3334) (Thanks Paul Mathew!)
- perf: build partition filter with balanced tree to avoid RecursionError (#3264) (Thanks Yingjian Wu!)
- fix: SaslServer busy-loop causes process hang after test suite (#3305) (Thanks Kevin Liu!)
- Initial work for file format writer API (#3119) (Thanks Neelesh Salian!)
- Bump daft dependency to >=0.7.10 (fix Python 3.14 compatibility) (#3323) (Thanks Kevin Liu!)
- Build: Bump fastavro from 1.12.1 to 1.12.2 (#3310) (Thanks dependabot[bot]!)
- Build: Bump rich from 14.3.3 to 15.0.0 (#3283) (Thanks dependabot[bot]!)

## apache/iceberg-rust

### Rust

_Top 20 themes from 37 scored commits._

- Encryption: add key management and encrypted IO support (#2339, #2340) (Thanks Xander and Claude Opus 4.6 (1M context)!)
- feat(reader): Add read_with_metrics() for scan I/O metrics (#2349) (Thanks Matt Butrovich, Claude Opus 4.6 (1M context), and blackmwk!)
- fix(catalog/memory): relax strict ms inequality in test_update_table (#2395) (Thanks Kurtis Wright!)
- feat(schema): Add `update_schema` action to enable table schema updates (#2120) (Thanks Victor Ghita and Claude Sonnet 4.6!)
- fix(sqllogictest): add missing tokio `rt-multi-thread` feature (#2386) (Thanks Charles-Antoine Leger!)
- fix: allow missing sequence-number in v2 snapshots for v1-upgraded tables (#2127) (Thanks Jem Bishop!)
- feat(datatypes): add optional and required constructors for MapType (#2405) (Thanks Liang Gong!)
- fix: NaN pushdown correctly pushes down NaNs correctness issue  (#2351) (Thanks Xander!)
- chore: Improve release process (#2381) (Thanks Shawn Chang!)
- Split arrow reader into smaller modules (#2358) (Thanks blackmwk and Claude Opus 4.7 (1M context)!)
- docs: bump version for python binding (#2377) (Thanks Kevin Liu!)
- Fix RUSTSEC-2026-0122 (#2437) (Thanks blackmwk!)
- fix(transaction): fix previous snapshot summary fetching (#2391) (Thanks dentiny!)
- CI: Use specific patch versions in workflow action comments (#2412) (Thanks Kevin Liu!)
- feat(datafusion): show pushed-down limit in IcebergTableScan EXPLAIN output (#2360) (Thanks Charles-Antoine Leger!)
- fix(tests): remove unnecessary `.to_string()` calls for metadata_location (#2407) (Thanks Liang Gong!)
- docs: Correct docs for Int128 and UInt128 being big-endian not little-endian (#2397) (Thanks Xander!)
- docs(arrow): clarify ScanMetrics::bytes_read includes delete files (#2379) (Thanks Matt Butrovich!)
- ci(python): verify wheel abi3 compatibility with --no-build (#2388) (Thanks Kevin Liu!)
- chore(deps): bump opendal to 0.56, migrate to reqsign-core 3.0 (#2401) (Thanks Krisztián Szűcs!)

## apache/iceberg-go

### Go

_Top 20 themes from 65 scored commits._

- Compaction and rewrite data files: expand rewrite planning and execution (#928, #934, #947, #948, #1033) (Thanks Tobias Pütz and Andrei Tserakhau!)
- Deletion vectors: add read, write, and validation support (#866, #1041) (Thanks Andrei Tserakhau and Shreyas Mishra!)
- feat(catalog): add version-hint management for Hadoop catalog (Thanks Tanmay Rauth!)
- feat(io): add BulkRemovableIO interface(#914) (#916) (Thanks Tanmay Rauth!)
- test(table): add v3 OCC row lineage regression tests (#998) (#1043) (Thanks Tanmay Rauth!)
- test(table): add round-trip test for v3 metadata with partition-statistics (#1012) (#1019) (Thanks Tanmay Rauth!)
- feat(cli): add maintenance command wiring and stubs (#1073) (Thanks Tanmay Rauth!)
- fix(manifest): allow ManifestListWriter to reference lower-version manifests (#1030) (Thanks Ashley Jeffs!)
- feat(io): add ListableIO interface to replace reflect-based directory walking (#913) (#917) (Thanks Tanmay Rauth!)
- fix(occ): manifest list rebuild (#982) (Thanks Masa and masa hoashi!)
- feat(config,cmd/iceberg): support more rest options in config (#933) (Thanks Matt Topol!)
- feat(cli): add partition-stats command (#1065) (Thanks Tanmay Rauth!)
- fix(manifest): restore data_file.distinct_counts on v1/v2 Avro schemas (#1044) (Thanks Masa!)
- feat(catalog): add hadoop namespace operations (#963) (Thanks Tanmay Rauth!)
- feat(catalog): add Hadoop catalog scaffold with path helpers (#953) (Thanks Tanmay Rauth!)
- feat(table): support zstd metadata compression codec (#1020) (Thanks Tanmay Rauth!)
- feat(manifest): Add tests for Entries and migrate snapshotProducer (#1031) (Thanks Artem Alperin!)
- feat(io): add native in-memory FS (#1025) (Thanks Alessandro Nori!)
- fix(io): resolve S3 PermanentRedirect for S3 Table Buckets (#974) (#975) (Thanks Tanmay Rauth!)
- feat(manifest): omit data_file.distinct_counts on v3 manifests (#1039) (Thanks Masa!)

## apache/iceberg-cpp

### C++

_Top 19 themes from 19 scored commits._

- feat(io): add streaming FileIO support (#641) (Thanks Gang Wu!)
- feat: add iceberg_data library alongside iceberg (#631) (Thanks Junwang Zhao!)
- fix: typo in RoaringPositionBitmap deletion vector note (#632) (Thanks Junwang Zhao!)
- feat(data): add delete filter support (#650) (Thanks Gang Wu!)
- feat: add ReachableFileCleanup to expire snapshots (#592) (Thanks Xinli Shang!)
- feat: retry failed transaction commit (#626) (Thanks SkylerLin!)
- fix: concurrent Lazy::Get should get correct result (#634) (Thanks Zehua Zou!)
- fix: repair shared package linkage and export scan builder symbols (#635) (Thanks Junwang Zhao!)
- refactor(util): make retry policy explicit and deterministic (#633) (Thanks Gang Wu!)
- fix(cmake): use consistent generator expressions to link libraries (#639) (Thanks Junwang Zhao!)
- CI: Use specific patch versions in workflow action comments (#644) (Thanks Kevin Liu!)
- ci: split S3/MinIO into a Linux and macOS-only workflow (#642) (Thanks Junwang Zhao!)
- ci: use ilammy/msvc-dev-cmd for Windows MSVC environment (#643) (Thanks Junwang Zhao!)
- fix(ci): restore auth for docs gh-pages deploy (#625) (Thanks Gang Wu and Kevin Liu!)
- chore: bump arrow-cpp to 24.0.0 (#623) (Thanks Gang Wu!)
- chore(deps): bump github/codeql-action from 4.35.2 to 4.35.3 (#647) (Thanks dependabot[bot]!)
- chore(deps): bump mozilla-actions/sccache-action from 0.0.9 to 0.0.10 (#636) (Thanks dependabot[bot]!)
- chore(deps): bump zizmorcore/zizmor-action from 0.5.2 to 0.5.3 (#630) (Thanks dependabot[bot]!)
- chore(deps): bump github/codeql-action from 4.35.1 to 4.35.2 (#629) (Thanks dependabot[bot]!)
