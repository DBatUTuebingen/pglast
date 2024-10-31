# -*- coding: utf-8 -*-
# :Project:   pglast — DO NOT EDIT: automatically extracted from nodes.h @ 17-latest-0-g7fb9821
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017-2024 Lele Gaifax
#

from enum import Enum, IntEnum, IntFlag, auto

try:
    from enum import StrEnum
except ImportError:  # pragma: no cover
    # Python < 3.10
    class StrEnum(str, Enum):
        pass


class AggSplit(IntEnum):
    AGGSPLIT_SIMPLE = 0
    AGGSPLIT_INITIAL_SERIAL = 0x02 | 0x04
    AGGSPLIT_FINAL_DESERIAL = 0x01 | 0x08


class AggStrategy(IntEnum):
    AGG_PLAIN = 0
    AGG_SORTED = auto()
    AGG_HASHED = auto()
    AGG_MIXED = auto()


class CmdType(IntEnum):
    CMD_UNKNOWN = 0
    CMD_SELECT = auto()
    CMD_UPDATE = auto()
    CMD_INSERT = auto()
    CMD_DELETE = auto()
    CMD_MERGE = auto()
    CMD_UTILITY = auto()
    CMD_NOTHING = auto()


class JoinType(IntEnum):
    JOIN_INNER = 0
    JOIN_LEFT = auto()
    JOIN_FULL = auto()
    JOIN_RIGHT = auto()
    JOIN_SEMI = auto()
    JOIN_ANTI = auto()
    JOIN_RIGHT_ANTI = auto()
    JOIN_UNIQUE_OUTER = auto()
    JOIN_UNIQUE_INNER = auto()


class LimitOption(IntEnum):
    LIMIT_OPTION_DEFAULT = 0
    LIMIT_OPTION_COUNT = auto()
    LIMIT_OPTION_WITH_TIES = auto()


class NodeTag(IntEnum):
    T_Invalid = 0
    T_List = 1
    T_Alias = 2
    T_RangeVar = 3
    T_TableFunc = 4
    T_IntoClause = 5
    T_Var = 6
    T_Const = 7
    T_Param = 8
    T_Aggref = 9
    T_GroupingFunc = 10
    T_WindowFunc = 11
    T_WindowFuncRunCondition = 12
    T_MergeSupportFunc = 13
    T_SubscriptingRef = 14
    T_FuncExpr = 15
    T_NamedArgExpr = 16
    T_OpExpr = 17
    T_DistinctExpr = 18
    T_NullIfExpr = 19
    T_ScalarArrayOpExpr = 20
    T_BoolExpr = 21
    T_SubLink = 22
    T_SubPlan = 23
    T_AlternativeSubPlan = 24
    T_FieldSelect = 25
    T_FieldStore = 26
    T_RelabelType = 27
    T_CoerceViaIO = 28
    T_ArrayCoerceExpr = 29
    T_ConvertRowtypeExpr = 30
    T_CollateExpr = 31
    T_CaseExpr = 32
    T_CaseWhen = 33
    T_CaseTestExpr = 34
    T_ArrayExpr = 35
    T_RowExpr = 36
    T_RowCompareExpr = 37
    T_CoalesceExpr = 38
    T_MinMaxExpr = 39
    T_SQLValueFunction = 40
    T_XmlExpr = 41
    T_JsonFormat = 42
    T_JsonReturning = 43
    T_JsonValueExpr = 44
    T_JsonConstructorExpr = 45
    T_JsonIsPredicate = 46
    T_JsonBehavior = 47
    T_JsonExpr = 48
    T_JsonTablePath = 49
    T_JsonTablePathScan = 50
    T_JsonTableSiblingJoin = 51
    T_NullTest = 52
    T_BooleanTest = 53
    T_MergeAction = 54
    T_CoerceToDomain = 55
    T_CoerceToDomainValue = 56
    T_SetToDefault = 57
    T_CurrentOfExpr = 58
    T_NextValueExpr = 59
    T_InferenceElem = 60
    T_TargetEntry = 61
    T_RangeTblRef = 62
    T_JoinExpr = 63
    T_FromExpr = 64
    T_OnConflictExpr = 65
    T_Query = 66
    T_TypeName = 67
    T_ColumnRef = 68
    T_ParamRef = 69
    T_A_Expr = 70
    T_A_Const = 71
    T_TypeCast = 72
    T_CollateClause = 73
    T_RoleSpec = 74
    T_FuncCall = 75
    T_A_Star = 76
    T_A_Indices = 77
    T_A_Indirection = 78
    T_A_ArrayExpr = 79
    T_ResTarget = 80
    T_MultiAssignRef = 81
    T_SortBy = 82
    T_WindowDef = 83
    T_RangeSubselect = 84
    T_RangeFunction = 85
    T_RangeTableFunc = 86
    T_RangeTableFuncCol = 87
    T_RangeTableSample = 88
    T_ColumnDef = 89
    T_TableLikeClause = 90
    T_IndexElem = 91
    T_DefElem = 92
    T_LockingClause = 93
    T_XmlSerialize = 94
    T_PartitionElem = 95
    T_PartitionSpec = 96
    T_PartitionBoundSpec = 97
    T_PartitionRangeDatum = 98
    T_SinglePartitionSpec = 99
    T_PartitionCmd = 100
    T_RangeTblEntry = 101
    T_RTEPermissionInfo = 102
    T_RangeTblFunction = 103
    T_TableSampleClause = 104
    T_WithCheckOption = 105
    T_SortGroupClause = 106
    T_GroupingSet = 107
    T_WindowClause = 108
    T_RowMarkClause = 109
    T_WithClause = 110
    T_InferClause = 111
    T_OnConflictClause = 112
    T_CTESearchClause = 113
    T_CTECycleClause = 114
    T_CommonTableExpr = 115
    T_MergeWhenClause = 116
    T_TriggerTransition = 117
    T_JsonOutput = 118
    T_JsonArgument = 119
    T_JsonFuncExpr = 120
    T_JsonTablePathSpec = 121
    T_JsonTable = 122
    T_JsonTableColumn = 123
    T_JsonKeyValue = 124
    T_JsonParseExpr = 125
    T_JsonScalarExpr = 126
    T_JsonSerializeExpr = 127
    T_JsonObjectConstructor = 128
    T_JsonArrayConstructor = 129
    T_JsonArrayQueryConstructor = 130
    T_JsonAggConstructor = 131
    T_JsonObjectAgg = 132
    T_JsonArrayAgg = 133
    T_RawStmt = 134
    T_InsertStmt = 135
    T_DeleteStmt = 136
    T_UpdateStmt = 137
    T_MergeStmt = 138
    T_SelectStmt = 139
    T_SetOperationStmt = 140
    T_ReturnStmt = 141
    T_PLAssignStmt = 142
    T_CreateSchemaStmt = 143
    T_AlterTableStmt = 144
    T_ReplicaIdentityStmt = 145
    T_AlterTableCmd = 146
    T_AlterCollationStmt = 147
    T_AlterDomainStmt = 148
    T_GrantStmt = 149
    T_ObjectWithArgs = 150
    T_AccessPriv = 151
    T_GrantRoleStmt = 152
    T_AlterDefaultPrivilegesStmt = 153
    T_CopyStmt = 154
    T_VariableSetStmt = 155
    T_VariableShowStmt = 156
    T_CreateStmt = 157
    T_Constraint = 158
    T_CreateTableSpaceStmt = 159
    T_DropTableSpaceStmt = 160
    T_AlterTableSpaceOptionsStmt = 161
    T_AlterTableMoveAllStmt = 162
    T_CreateExtensionStmt = 163
    T_AlterExtensionStmt = 164
    T_AlterExtensionContentsStmt = 165
    T_CreateFdwStmt = 166
    T_AlterFdwStmt = 167
    T_CreateForeignServerStmt = 168
    T_AlterForeignServerStmt = 169
    T_CreateForeignTableStmt = 170
    T_CreateUserMappingStmt = 171
    T_AlterUserMappingStmt = 172
    T_DropUserMappingStmt = 173
    T_ImportForeignSchemaStmt = 174
    T_CreatePolicyStmt = 175
    T_AlterPolicyStmt = 176
    T_CreateAmStmt = 177
    T_CreateTrigStmt = 178
    T_CreateEventTrigStmt = 179
    T_AlterEventTrigStmt = 180
    T_CreatePLangStmt = 181
    T_CreateRoleStmt = 182
    T_AlterRoleStmt = 183
    T_AlterRoleSetStmt = 184
    T_DropRoleStmt = 185
    T_CreateSeqStmt = 186
    T_AlterSeqStmt = 187
    T_DefineStmt = 188
    T_CreateDomainStmt = 189
    T_CreateOpClassStmt = 190
    T_CreateOpClassItem = 191
    T_CreateOpFamilyStmt = 192
    T_AlterOpFamilyStmt = 193
    T_DropStmt = 194
    T_TruncateStmt = 195
    T_CommentStmt = 196
    T_SecLabelStmt = 197
    T_DeclareCursorStmt = 198
    T_ClosePortalStmt = 199
    T_FetchStmt = 200
    T_IndexStmt = 201
    T_CreateStatsStmt = 202
    T_StatsElem = 203
    T_AlterStatsStmt = 204
    T_CreateFunctionStmt = 205
    T_FunctionParameter = 206
    T_AlterFunctionStmt = 207
    T_DoStmt = 208
    T_InlineCodeBlock = 209
    T_CallStmt = 210
    T_CallContext = 211
    T_RenameStmt = 212
    T_AlterObjectDependsStmt = 213
    T_AlterObjectSchemaStmt = 214
    T_AlterOwnerStmt = 215
    T_AlterOperatorStmt = 216
    T_AlterTypeStmt = 217
    T_RuleStmt = 218
    T_NotifyStmt = 219
    T_ListenStmt = 220
    T_UnlistenStmt = 221
    T_TransactionStmt = 222
    T_CompositeTypeStmt = 223
    T_CreateEnumStmt = 224
    T_CreateRangeStmt = 225
    T_AlterEnumStmt = 226
    T_ViewStmt = 227
    T_LoadStmt = 228
    T_CreatedbStmt = 229
    T_AlterDatabaseStmt = 230
    T_AlterDatabaseRefreshCollStmt = 231
    T_AlterDatabaseSetStmt = 232
    T_DropdbStmt = 233
    T_AlterSystemStmt = 234
    T_ClusterStmt = 235
    T_VacuumStmt = 236
    T_VacuumRelation = 237
    T_ExplainStmt = 238
    T_CreateTableAsStmt = 239
    T_RefreshMatViewStmt = 240
    T_CheckPointStmt = 241
    T_DiscardStmt = 242
    T_LockStmt = 243
    T_ConstraintsSetStmt = 244
    T_ReindexStmt = 245
    T_CreateConversionStmt = 246
    T_CreateCastStmt = 247
    T_CreateTransformStmt = 248
    T_PrepareStmt = 249
    T_ExecuteStmt = 250
    T_DeallocateStmt = 251
    T_DropOwnedStmt = 252
    T_ReassignOwnedStmt = 253
    T_AlterTSDictionaryStmt = 254
    T_AlterTSConfigurationStmt = 255
    T_PublicationTable = 256
    T_PublicationObjSpec = 257
    T_CreatePublicationStmt = 258
    T_AlterPublicationStmt = 259
    T_CreateSubscriptionStmt = 260
    T_AlterSubscriptionStmt = 261
    T_DropSubscriptionStmt = 262
    T_PlannerGlobal = 263
    T_PlannerInfo = 264
    T_RelOptInfo = 265
    T_IndexOptInfo = 266
    T_ForeignKeyOptInfo = 267
    T_StatisticExtInfo = 268
    T_JoinDomain = 269
    T_EquivalenceClass = 270
    T_EquivalenceMember = 271
    T_PathKey = 272
    T_GroupByOrdering = 273
    T_PathTarget = 274
    T_ParamPathInfo = 275
    T_Path = 276
    T_IndexPath = 277
    T_IndexClause = 278
    T_BitmapHeapPath = 279
    T_BitmapAndPath = 280
    T_BitmapOrPath = 281
    T_TidPath = 282
    T_TidRangePath = 283
    T_SubqueryScanPath = 284
    T_ForeignPath = 285
    T_CustomPath = 286
    T_AppendPath = 287
    T_MergeAppendPath = 288
    T_GroupResultPath = 289
    T_MaterialPath = 290
    T_MemoizePath = 291
    T_UniquePath = 292
    T_GatherPath = 293
    T_GatherMergePath = 294
    T_NestPath = 295
    T_MergePath = 296
    T_HashPath = 297
    T_ProjectionPath = 298
    T_ProjectSetPath = 299
    T_SortPath = 300
    T_IncrementalSortPath = 301
    T_GroupPath = 302
    T_UpperUniquePath = 303
    T_AggPath = 304
    T_GroupingSetData = 305
    T_RollupData = 306
    T_GroupingSetsPath = 307
    T_MinMaxAggPath = 308
    T_WindowAggPath = 309
    T_SetOpPath = 310
    T_RecursiveUnionPath = 311
    T_LockRowsPath = 312
    T_ModifyTablePath = 313
    T_LimitPath = 314
    T_RestrictInfo = 315
    T_PlaceHolderVar = 316
    T_SpecialJoinInfo = 317
    T_OuterJoinClauseInfo = 318
    T_AppendRelInfo = 319
    T_RowIdentityVarInfo = 320
    T_PlaceHolderInfo = 321
    T_MinMaxAggInfo = 322
    T_PlannerParamItem = 323
    T_AggInfo = 324
    T_AggTransInfo = 325
    T_PlannedStmt = 326
    T_Result = 327
    T_ProjectSet = 328
    T_ModifyTable = 329
    T_Append = 330
    T_MergeAppend = 331
    T_RecursiveUnion = 332
    T_BitmapAnd = 333
    T_BitmapOr = 334
    T_SeqScan = 335
    T_SampleScan = 336
    T_IndexScan = 337
    T_IndexOnlyScan = 338
    T_BitmapIndexScan = 339
    T_BitmapHeapScan = 340
    T_TidScan = 341
    T_TidRangeScan = 342
    T_SubqueryScan = 343
    T_FunctionScan = 344
    T_ValuesScan = 345
    T_TableFuncScan = 346
    T_CteScan = 347
    T_NamedTuplestoreScan = 348
    T_WorkTableScan = 349
    T_ForeignScan = 350
    T_CustomScan = 351
    T_NestLoop = 352
    T_NestLoopParam = 353
    T_MergeJoin = 354
    T_HashJoin = 355
    T_Material = 356
    T_Memoize = 357
    T_Sort = 358
    T_IncrementalSort = 359
    T_Group = 360
    T_Agg = 361
    T_WindowAgg = 362
    T_Unique = 363
    T_Gather = 364
    T_GatherMerge = 365
    T_Hash = 366
    T_SetOp = 367
    T_LockRows = 368
    T_Limit = 369
    T_PlanRowMark = 370
    T_PartitionPruneInfo = 371
    T_PartitionedRelPruneInfo = 372
    T_PartitionPruneStepOp = 373
    T_PartitionPruneStepCombine = 374
    T_PlanInvalItem = 375
    T_ExprState = 376
    T_IndexInfo = 377
    T_ExprContext = 378
    T_ReturnSetInfo = 379
    T_ProjectionInfo = 380
    T_JunkFilter = 381
    T_OnConflictSetState = 382
    T_MergeActionState = 383
    T_ResultRelInfo = 384
    T_EState = 385
    T_WindowFuncExprState = 386
    T_SetExprState = 387
    T_SubPlanState = 388
    T_DomainConstraintState = 389
    T_ResultState = 390
    T_ProjectSetState = 391
    T_ModifyTableState = 392
    T_AppendState = 393
    T_MergeAppendState = 394
    T_RecursiveUnionState = 395
    T_BitmapAndState = 396
    T_BitmapOrState = 397
    T_ScanState = 398
    T_SeqScanState = 399
    T_SampleScanState = 400
    T_IndexScanState = 401
    T_IndexOnlyScanState = 402
    T_BitmapIndexScanState = 403
    T_BitmapHeapScanState = 404
    T_TidScanState = 405
    T_TidRangeScanState = 406
    T_SubqueryScanState = 407
    T_FunctionScanState = 408
    T_ValuesScanState = 409
    T_TableFuncScanState = 410
    T_CteScanState = 411
    T_NamedTuplestoreScanState = 412
    T_WorkTableScanState = 413
    T_ForeignScanState = 414
    T_CustomScanState = 415
    T_JoinState = 416
    T_NestLoopState = 417
    T_MergeJoinState = 418
    T_HashJoinState = 419
    T_MaterialState = 420
    T_MemoizeState = 421
    T_SortState = 422
    T_IncrementalSortState = 423
    T_GroupState = 424
    T_AggState = 425
    T_WindowAggState = 426
    T_UniqueState = 427
    T_GatherState = 428
    T_GatherMergeState = 429
    T_HashState = 430
    T_SetOpState = 431
    T_LockRowsState = 432
    T_LimitState = 433
    T_IndexAmRoutine = 434
    T_TableAmRoutine = 435
    T_TsmRoutine = 436
    T_EventTriggerData = 437
    T_TriggerData = 438
    T_TupleTableSlot = 439
    T_FdwRoutine = 440
    T_Bitmapset = 441
    T_ExtensibleNode = 442
    T_ErrorSaveContext = 443
    T_IdentifySystemCmd = 444
    T_BaseBackupCmd = 445
    T_CreateReplicationSlotCmd = 446
    T_DropReplicationSlotCmd = 447
    T_AlterReplicationSlotCmd = 448
    T_StartReplicationCmd = 449
    T_ReadReplicationSlotCmd = 450
    T_TimeLineHistoryCmd = 451
    T_UploadManifestCmd = 452
    T_SupportRequestSimplify = 453
    T_SupportRequestSelectivity = 454
    T_SupportRequestCost = 455
    T_SupportRequestRows = 456
    T_SupportRequestIndexCondition = 457
    T_SupportRequestWFuncMonotonic = 458
    T_SupportRequestOptimizeWindowClause = 459
    T_Integer = 460
    T_Float = 461
    T_Boolean = 462
    T_String = 463
    T_BitString = 464
    T_ForeignKeyCacheInfo = 465
    T_IntList = 466
    T_OidList = 467
    T_XidList = 468
    T_AllocSetContext = 469
    T_GenerationContext = 470
    T_SlabContext = 471
    T_BumpContext = 472
    T_TIDBitmap = 473
    T_WindowObjectData = 474


class OnConflictAction(IntEnum):
    ONCONFLICT_NONE = 0
    ONCONFLICT_NOTHING = auto()
    ONCONFLICT_UPDATE = auto()


class SetOpCmd(IntEnum):
    SETOPCMD_INTERSECT = 0
    SETOPCMD_INTERSECT_ALL = auto()
    SETOPCMD_EXCEPT = auto()
    SETOPCMD_EXCEPT_ALL = auto()


class SetOpStrategy(IntEnum):
    SETOP_SORTED = 0
    SETOP_HASHED = auto()


# #define-ed constants

AGGSPLITOP_COMBINE = 0x01

AGGSPLITOP_SKIPFINAL = 0x02

AGGSPLITOP_SERIALIZE = 0x04

AGGSPLITOP_DESERIALIZE = 0x08
