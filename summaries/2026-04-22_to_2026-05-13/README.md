# Iceberg Community Sync Summary

- Period: `2026-04-22` to before `2026-05-13`
- Review candidates: `182`

## apache/iceberg

### Java

_Top 20 of 131 scored commits._

- Core: Add implementations of v4 TrackedFile interfaces (#15854) (Thanks Anoop Johnson!)
- Spark: Support writing shredded variant in Iceberg-Spark (#14297) (Thanks Aihua Xu and Neelesh Salian!)
- Spark: Backport support writing shredded variant in Iceberg-Spark (#16241) (Thanks pvary!)
- Core: Add builders for v4 structs (#16092) (Thanks Anoop Johnson and Eduard Tudenhoefner!)
- Core, Catalogs: Add support for unique table locations via catalog property (#12892) (Thanks Dmitriy Avseitsev!)
- Spark: backport PR #15512 to v3.4, v3.5, v4.0 for WAP branch delete fix (#16245) (Thanks Steven Zhen Wu and Claude Opus 4.7 (1M context)!)
- Spark: Fix LICENSE/NOTICE compliance for all versions of spark-runtime (v3.4, v3.5, v4.0, v4.1) (#16215) (Thanks Kevin Liu!)
- Core: Fix row ID assignment for EXISTING entry during a manifest merge (#16263) (Thanks Amogh Jahagirdar, ChengJi, and Russell Spitzer!)
- Flink: Add Nanosecond Precision Support for Flink-Iceberg Integration (#15475) (Thanks Talat UYARER!)
- Core: Add partition to TrackedFile (#16253) (Thanks Eduard Tudenhoefner!)
- Flink: Fix JdbcLockFactory to allow ClientPoolImpl connection retry (#16049) (Thanks Anupam Yadav!)
- Flink: Backport add Nanosecond Precision Support for Flink-Iceberg Integration to Flink 1.20 (#16240) (Thanks pvary!)
- Spark: Add unknown type support to Spark 3.4 and 3.5 (#16066) (Thanks Kurtis Wright!)
- Core, AWS: Adapt code to S3 signing endpoint promotion (#15451) (Thanks Alexandre Dutra!)
- Kafka Connect: Add Trivy CVE scan to CI (#15430) (#15430) (Thanks Robin Moffatt and Claude Opus 4.6!)
- Flink: Backport add Nanosecond Precision Support for Flink-Iceberg Integration (#16183) (Thanks Talat UYARER!)
- Spark, Hive: Fix snapshot procedure for tables with Variant columns (#15964) (Thanks Neelesh Salian!)
- ORC: Add _row_id and _last_updated_sequence_number raeder in Orc to support lineage (#15776) (Thanks GuoYu!)
- Flink:Backport RewriteDataFile support dynamic filter (#16132) (Thanks GuoYu!)
- Spark: Support TimestampNTZ in SparkZOrderUDF (#15778) (Thanks milleniax and abdullin.marsel9!)

## apache/iceberg-python

### Python

_Top 20 of 51 scored commits._

- Add support for 'overwrite' option in register_table (#3290) (Thanks Yuya Ebihara!)
- Add support for registering views (#3288) (Thanks Yuya Ebihara!)
- infra: add python 3.14 support (#3299) (Thanks Adam and Kevin Liu!)
- feat: add load_view to REST catalog (#3224) (Thanks spr0els!)
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
- Bump daft dependency to >=0.7.10 (fix Python 3.14 compatibility) (#3323) (Thanks Kevin Liu!)
- perf: build partition filter with balanced tree to avoid RecursionError (#3264) (Thanks Yingjian Wu!)
- fix: SaslServer busy-loop causes process hang after test suite (#3305) (Thanks Kevin Liu!)
- Initial work for file format writer API (#3119) (Thanks Neelesh Salian!)
- Build: Bump fastavro from 1.12.1 to 1.12.2 (#3310) (Thanks dependabot[bot]!)
