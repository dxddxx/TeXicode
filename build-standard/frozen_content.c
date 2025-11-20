//
// Content for MICROPY_MODULE_FROZEN_STR
//
#include <stdint.h>
#define MP_FROZEN_STR_NAMES \

const uint32_t mp_frozen_str_sizes[] = { 0 };
const char mp_frozen_str_content[] = {
"\0"
};

//
// Content for MICROPY_MODULE_FROZEN_MPY
//
#include "py/mpconfig.h"
#include "py/objint.h"
#include "py/objstr.h"
#include "py/emitglue.h"
#include "py/nativeglue.h"

#if MICROPY_LONGINT_IMPL != 2
#error "incompatible MICROPY_LONGINT_IMPL"
#endif

#if MPZ_DIG_SIZE != 16
#error "incompatible MPZ_DIG_SIZE"
#endif

#if MICROPY_PY_BUILTINS_FLOAT
typedef struct _mp_obj_float_t {
    mp_obj_base_t base;
    mp_float_t value;
} mp_obj_float_t;
#endif

#if MICROPY_PY_BUILTINS_COMPLEX
typedef struct _mp_obj_complex_t {
    mp_obj_base_t base;
    mp_float_t real;
    mp_float_t imag;
} mp_obj_complex_t;
#endif

enum {
    MP_QSTR_Event = MP_QSTRnumber_of,
    MP_QSTR_Lock,
    MP_QSTR_Lock_space_not_space_acquired,
    MP_QSTR_Loop,
    MP_QSTR_SingletonGenerator,
    MP_QSTR_ThreadSafeFlag,
    MP_QSTR_TimeoutError,
    MP_QSTR__Remove,
    MP_QSTR___version__,
    MP_QSTR__exc_context,
    MP_QSTR__exc_handler,
    MP_QSTR__io_queue,
    MP_QSTR__promote_to_task,
    MP_QSTR__run,
    MP_QSTR__run_iter,
    MP_QSTR__schedule_run_iter,
    MP_QSTR_acquire,
    MP_QSTR_asyncio_slash___init___dot_py,
    MP_QSTR_asyncio_slash_core_dot_py,
    MP_QSTR_asyncio_slash_event_dot_py,
    MP_QSTR_asyncio_slash_funcs_dot_py,
    MP_QSTR_asyncio_slash_lock_dot_py,
    MP_QSTR_asyncio_timer,
    MP_QSTR_aw,
    MP_QSTR_call_exception_handler,
    MP_QSTR_can_squot_t_space_gather,
    MP_QSTR_clearTimeout,
    MP_QSTR_context,
    MP_QSTR_coro_equals_,
    MP_QSTR_coroutine_space_expected,
    MP_QSTR_create_task,
    MP_QSTR_current_task,
    MP_QSTR_default_exception_handler,
    MP_QSTR_dt,
    MP_QSTR_er,
    MP_QSTR_error,
    MP_QSTR_event,
    MP_QSTR_exc,
    MP_QSTR_exc_type,
    MP_QSTR_exception,
    MP_QSTR_flags,
    MP_QSTR_funcs,
    MP_QSTR_future,
    MP_QSTR_future_colon_,
    MP_QSTR_gather,
    MP_QSTR_get_event_loop,
    MP_QSTR_get_exception_handler,
    MP_QSTR_handler,
    MP_QSTR_is_set,
    MP_QSTR_lock,
    MP_QSTR_locked,
    MP_QSTR_loop,
    MP_QSTR_message,
    MP_QSTR_new_event_loop,
    MP_QSTR_queue_read,
    MP_QSTR_reject,
    MP_QSTR_release,
    MP_QSTR_req,
    MP_QSTR_resolve,
    MP_QSTR_result,
    MP_QSTR_return_exceptions,
    MP_QSTR_setTimeout,
    MP_QSTR_set_exception_handler,
    MP_QSTR_sgen,
    MP_QSTR_t,
    MP_QSTR_task,
    MP_QSTR_tb,
    MP_QSTR_then,
    MP_QSTR_thenable,
    MP_QSTR_ticks,
    MP_QSTR_timeout,
    MP_QSTR_wait_for,
    MP_QSTR_wait_for_ms,
    MP_QSTR_waiter,
    MP_QSTR_waiting,
};

const qstr_hash_t mp_qstr_frozen_const_hashes[] = {
    35561,
    59534,
    43943,
    59673,
    12601,
    9558,
    19302,
    37244,
    38975,
    13092,
    52355,
    43474,
    24914,
    58803,
    9926,
    52892,
    54045,
    63415,
    61558,
    25345,
    46624,
    16486,
    60125,
    28211,
    19688,
    4535,
    13127,
    55546,
    21001,
    50473,
    21139,
    8734,
    45889,
    28053,
    28082,
    4541,
    27081,
    9435,
    52220,
    60370,
    36858,
    27400,
    14592,
    22842,
    2184,
    19971,
    60604,
    24029,
    58562,
    9134,
    47631,
    9273,
    48238,
    3209,
    52601,
    63978,
    36844,
    35683,
    31889,
    47468,
    47572,
    35772,
    5288,
    32154,
    46545,
    40488,
    28563,
    48690,
    54168,
    2115,
    21566,
    40746,
    25035,
    60665,
    31214,
};

const qstr_len_t mp_qstr_frozen_const_lengths[] = {
    5,
    4,
    17,
    4,
    18,
    14,
    12,
    7,
    11,
    12,
    12,
    9,
    16,
    4,
    9,
    18,
    7,
    19,
    15,
    16,
    16,
    15,
    13,
    2,
    22,
    12,
    12,
    7,
    5,
    18,
    11,
    12,
    25,
    2,
    2,
    5,
    5,
    3,
    8,
    9,
    5,
    5,
    6,
    7,
    6,
    14,
    21,
    7,
    6,
    4,
    6,
    4,
    7,
    14,
    10,
    6,
    7,
    3,
    7,
    6,
    17,
    10,
    21,
    4,
    1,
    4,
    2,
    4,
    8,
    5,
    7,
    8,
    11,
    6,
    7,
};

extern const qstr_pool_t mp_qstr_const_pool;
const qstr_pool_t mp_qstr_frozen_const_pool = {
    &mp_qstr_const_pool, // previous pool
    MP_QSTRnumber_of, // previous pool size
    true, // is_sorted
    10, // allocated entries
    75, // used entries
    (qstr_hash_t *)mp_qstr_frozen_const_hashes,
    (qstr_len_t *)mp_qstr_frozen_const_lengths,
    {
        "Event",
        "Lock",
        "Lock not acquired",
        "Loop",
        "SingletonGenerator",
        "ThreadSafeFlag",
        "TimeoutError",
        "_Remove",
        "__version__",
        "_exc_context",
        "_exc_handler",
        "_io_queue",
        "_promote_to_task",
        "_run",
        "_run_iter",
        "_schedule_run_iter",
        "acquire",
        "asyncio/__init__.py",
        "asyncio/core.py",
        "asyncio/event.py",
        "asyncio/funcs.py",
        "asyncio/lock.py",
        "asyncio_timer",
        "aw",
        "call_exception_handler",
        "can't gather",
        "clearTimeout",
        "context",
        "coro=",
        "coroutine expected",
        "create_task",
        "current_task",
        "default_exception_handler",
        "dt",
        "er",
        "error",
        "event",
        "exc",
        "exc_type",
        "exception",
        "flags",
        "funcs",
        "future",
        "future:",
        "gather",
        "get_event_loop",
        "get_exception_handler",
        "handler",
        "is_set",
        "lock",
        "locked",
        "loop",
        "message",
        "new_event_loop",
        "queue_read",
        "reject",
        "release",
        "req",
        "resolve",
        "result",
        "return_exceptions",
        "setTimeout",
        "set_exception_handler",
        "sgen",
        "t",
        "task",
        "tb",
        "then",
        "thenable",
        "ticks",
        "timeout",
        "wait_for",
        "wait_for_ms",
        "waiter",
        "waiting",
    },
};

////////////////////////////////////////////////////////////////////////////////
// frozen module asyncio_event
// - original source file: build-standard/frozen_mpy/asyncio/event.mpy
// - frozen file name: asyncio/event.py
// - .mpy header: 4d:06:00:1f

// frozen bytecode for file asyncio/event.py, scope asyncio_event__lt_module_gt_
static const byte fun_data_asyncio_event__lt_module_gt_[59] = {
    0x2c,0x02, // prelude
    0x01, // names: <module>
     // code info
    0x81, // LOAD_CONST_SMALL_INT 1
    0x10,0x02, // LOAD_CONST_STRING 'core'
    0x2a,0x01, // BUILD_TUPLE 1
    0x1b,0x03, // IMPORT_NAME ''
    0x1c,0x02, // IMPORT_FROM 'core'
    0x16,0x02, // STORE_NAME 'core'
    0x59, // POP_TOP
    0x54, // LOAD_BUILD_CLASS
    0x32,0x00, // MAKE_FUNCTION 0
    0x10,0x04, // LOAD_CONST_STRING 'Event'
    0x34,0x02, // CALL_FUNCTION 2
    0x16,0x04, // STORE_NAME 'Event'
    0x48,0x15, // SETUP_EXCEPT 21
    0x80, // LOAD_CONST_SMALL_INT 0
    0x51, // LOAD_CONST_NONE
    0x1b,0x05, // IMPORT_NAME 'io'
    0x16,0x05, // STORE_NAME 'io'
    0x54, // LOAD_BUILD_CLASS
    0x32,0x01, // MAKE_FUNCTION 1
    0x10,0x06, // LOAD_CONST_STRING 'ThreadSafeFlag'
    0x11,0x05, // LOAD_NAME 'io'
    0x13,0x07, // LOAD_ATTR 'IOBase'
    0x34,0x03, // CALL_FUNCTION 3
    0x16,0x06, // STORE_NAME 'ThreadSafeFlag'
    0x4a,0x0a, // POP_EXCEPT_JUMP 10
    0x57, // DUP_TOP
    0x11,0x19, // LOAD_NAME 'ImportError'
    0xdf, // BINARY_OP 8 <exception match>
    0x44,0x43, // POP_JUMP_IF_FALSE 3
    0x59, // POP_TOP
    0x4a,0x01, // POP_EXCEPT_JUMP 1
    0x5d, // END_FINALLY
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
// child of asyncio_event__lt_module_gt_
// frozen bytecode for file asyncio/event.py, scope asyncio_event_Event
static const byte fun_data_asyncio_event_Event[33] = {
    0x00,0x02, // prelude
    0x04, // names: Event
     // code info
    0x11,0x1a, // LOAD_NAME '__name__'
    0x16,0x1b, // STORE_NAME '__module__'
    0x10,0x04, // LOAD_CONST_STRING 'Event'
    0x16,0x1c, // STORE_NAME '__qualname__'
    0x32,0x00, // MAKE_FUNCTION 0
    0x16,0x08, // STORE_NAME '__init__'
    0x32,0x01, // MAKE_FUNCTION 1
    0x16,0x0c, // STORE_NAME 'is_set'
    0x32,0x02, // MAKE_FUNCTION 2
    0x16,0x0d, // STORE_NAME 'set'
    0x32,0x03, // MAKE_FUNCTION 3
    0x16,0x12, // STORE_NAME 'clear'
    0x32,0x04, // MAKE_FUNCTION 4
    0x16,0x13, // STORE_NAME 'wait'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
// child of asyncio_event_Event
// frozen bytecode for file asyncio/event.py, scope asyncio_event_Event___init__
static const byte fun_data_asyncio_event_Event___init__[19] = {
    0x11,0x04, // prelude
    0x08,0x1d, // names: __init__, self
     // code info
    0x50, // LOAD_CONST_FALSE
    0xb0, // LOAD_FAST 0
    0x18,0x09, // STORE_ATTR 'state'
    0x12,0x02, // LOAD_GLOBAL 'core'
    0x14,0x0a, // LOAD_METHOD 'TaskQueue'
    0x36,0x00, // CALL_METHOD 0
    0xb0, // LOAD_FAST 0
    0x18,0x0b, // STORE_ATTR 'waiting'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_event_Event___init__ = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_event_Event___init__,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 19,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 3,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 8,
        .line_info = fun_data_asyncio_event_Event___init__ + 4,
        .line_info_top = fun_data_asyncio_event_Event___init__ + 4,
        .opcodes = fun_data_asyncio_event_Event___init__ + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_event_Event___init__ fun_data_asyncio_event_Event___init__[0]
#endif

// child of asyncio_event_Event
// frozen bytecode for file asyncio/event.py, scope asyncio_event_Event_is_set
static const byte fun_data_asyncio_event_Event_is_set[8] = {
    0x09,0x04, // prelude
    0x0c,0x1d, // names: is_set, self
     // code info
    0xb0, // LOAD_FAST 0
    0x13,0x09, // LOAD_ATTR 'state'
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_event_Event_is_set = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_event_Event_is_set,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 8,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 2,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 12,
        .line_info = fun_data_asyncio_event_Event_is_set + 4,
        .line_info_top = fun_data_asyncio_event_Event_is_set + 4,
        .opcodes = fun_data_asyncio_event_Event_is_set + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_event_Event_is_set fun_data_asyncio_event_Event_is_set[0]
#endif

// child of asyncio_event_Event
// frozen bytecode for file asyncio/event.py, scope asyncio_event_Event_set
static const byte fun_data_asyncio_event_Event_set[37] = {
    0x21,0x04, // prelude
    0x0d,0x1d, // names: set, self
     // code info
    0x42,0x50, // JUMP 16
    0x12,0x02, // LOAD_GLOBAL 'core'
    0x13,0x0e, // LOAD_ATTR '_task_queue'
    0x14,0x0f, // LOAD_METHOD 'push'
    0xb0, // LOAD_FAST 0
    0x13,0x0b, // LOAD_ATTR 'waiting'
    0x14,0x10, // LOAD_METHOD 'pop'
    0x36,0x00, // CALL_METHOD 0
    0x36,0x01, // CALL_METHOD 1
    0x59, // POP_TOP
    0xb0, // LOAD_FAST 0
    0x13,0x0b, // LOAD_ATTR 'waiting'
    0x14,0x11, // LOAD_METHOD 'peek'
    0x36,0x00, // CALL_METHOD 0
    0x43,0x27, // POP_JUMP_IF_TRUE -25
    0x52, // LOAD_CONST_TRUE
    0xb0, // LOAD_FAST 0
    0x18,0x09, // STORE_ATTR 'state'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_event_Event_set = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_event_Event_set,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 37,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 5,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 13,
        .line_info = fun_data_asyncio_event_Event_set + 4,
        .line_info_top = fun_data_asyncio_event_Event_set + 4,
        .opcodes = fun_data_asyncio_event_Event_set + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_event_Event_set fun_data_asyncio_event_Event_set[0]
#endif

// child of asyncio_event_Event
// frozen bytecode for file asyncio/event.py, scope asyncio_event_Event_clear
static const byte fun_data_asyncio_event_Event_clear[10] = {
    0x11,0x04, // prelude
    0x12,0x1d, // names: clear, self
     // code info
    0x50, // LOAD_CONST_FALSE
    0xb0, // LOAD_FAST 0
    0x18,0x09, // STORE_ATTR 'state'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_event_Event_clear = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_event_Event_clear,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 10,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 3,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 18,
        .line_info = fun_data_asyncio_event_Event_clear + 4,
        .line_info_top = fun_data_asyncio_event_Event_clear + 4,
        .opcodes = fun_data_asyncio_event_Event_clear + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_event_Event_clear fun_data_asyncio_event_Event_clear[0]
#endif

// child of asyncio_event_Event
// frozen bytecode for file asyncio/event.py, scope asyncio_event_Event_wait
static const byte fun_data_asyncio_event_Event_wait[36] = {
    0x99,0x40,0x04, // prelude
    0x13,0x1d, // names: wait, self
     // code info
    0xb0, // LOAD_FAST 0
    0x13,0x09, // LOAD_ATTR 'state'
    0x43,0x58, // POP_JUMP_IF_TRUE 24
    0xb0, // LOAD_FAST 0
    0x13,0x0b, // LOAD_ATTR 'waiting'
    0x14,0x0f, // LOAD_METHOD 'push'
    0x12,0x02, // LOAD_GLOBAL 'core'
    0x13,0x14, // LOAD_ATTR 'cur_task'
    0x36,0x01, // CALL_METHOD 1
    0x59, // POP_TOP
    0xb0, // LOAD_FAST 0
    0x13,0x0b, // LOAD_ATTR 'waiting'
    0x12,0x02, // LOAD_GLOBAL 'core'
    0x13,0x14, // LOAD_ATTR 'cur_task'
    0x18,0x15, // STORE_ATTR 'data'
    0x51, // LOAD_CONST_NONE
    0x67, // YIELD_VALUE
    0x59, // POP_TOP
    0x52, // LOAD_CONST_TRUE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_event_Event_wait = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 1,
    .fun_data = fun_data_asyncio_event_Event_wait,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 36,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 4,
        .n_exc_stack = 0,
        .scope_flags = 1,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 19,
        .line_info = fun_data_asyncio_event_Event_wait + 5,
        .line_info_top = fun_data_asyncio_event_Event_wait + 5,
        .opcodes = fun_data_asyncio_event_Event_wait + 5,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_event_Event_wait fun_data_asyncio_event_Event_wait[0]
#endif

static const mp_raw_code_t *const children_asyncio_event_Event[] = {
    (const mp_raw_code_t *)&proto_fun_asyncio_event_Event___init__,
    (const mp_raw_code_t *)&proto_fun_asyncio_event_Event_is_set,
    (const mp_raw_code_t *)&proto_fun_asyncio_event_Event_set,
    (const mp_raw_code_t *)&proto_fun_asyncio_event_Event_clear,
    (const mp_raw_code_t *)&proto_fun_asyncio_event_Event_wait,
};

static const mp_raw_code_truncated_t proto_fun_asyncio_event_Event = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_event_Event,
    .children = (void *)&children_asyncio_event_Event,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 33,
    .n_children = 5,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 1,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 0,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 4,
        .line_info = fun_data_asyncio_event_Event + 3,
        .line_info_top = fun_data_asyncio_event_Event + 3,
        .opcodes = fun_data_asyncio_event_Event + 3,
    },
    #endif
    #endif
};

// child of asyncio_event__lt_module_gt_
// frozen bytecode for file asyncio/event.py, scope asyncio_event_ThreadSafeFlag
static const byte fun_data_asyncio_event_ThreadSafeFlag[33] = {
    0x00,0x02, // prelude
    0x06, // names: ThreadSafeFlag
     // code info
    0x11,0x1a, // LOAD_NAME '__name__'
    0x16,0x1b, // STORE_NAME '__module__'
    0x10,0x06, // LOAD_CONST_STRING 'ThreadSafeFlag'
    0x16,0x1c, // STORE_NAME '__qualname__'
    0x32,0x00, // MAKE_FUNCTION 0
    0x16,0x08, // STORE_NAME '__init__'
    0x32,0x01, // MAKE_FUNCTION 1
    0x16,0x16, // STORE_NAME 'ioctl'
    0x32,0x02, // MAKE_FUNCTION 2
    0x16,0x0d, // STORE_NAME 'set'
    0x32,0x03, // MAKE_FUNCTION 3
    0x16,0x12, // STORE_NAME 'clear'
    0x32,0x04, // MAKE_FUNCTION 4
    0x16,0x13, // STORE_NAME 'wait'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
// child of asyncio_event_ThreadSafeFlag
// frozen bytecode for file asyncio/event.py, scope asyncio_event_ThreadSafeFlag___init__
static const byte fun_data_asyncio_event_ThreadSafeFlag___init__[10] = {
    0x11,0x04, // prelude
    0x08,0x1d, // names: __init__, self
     // code info
    0x80, // LOAD_CONST_SMALL_INT 0
    0xb0, // LOAD_FAST 0
    0x18,0x09, // STORE_ATTR 'state'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_event_ThreadSafeFlag___init__ = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_event_ThreadSafeFlag___init__,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 10,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 3,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 8,
        .line_info = fun_data_asyncio_event_ThreadSafeFlag___init__ + 4,
        .line_info_top = fun_data_asyncio_event_ThreadSafeFlag___init__ + 4,
        .opcodes = fun_data_asyncio_event_ThreadSafeFlag___init__ + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_event_ThreadSafeFlag___init__ fun_data_asyncio_event_ThreadSafeFlag___init__[0]
#endif

// child of asyncio_event_ThreadSafeFlag
// frozen bytecode for file asyncio/event.py, scope asyncio_event_ThreadSafeFlag_ioctl
static const byte fun_data_asyncio_event_ThreadSafeFlag_ioctl[19] = {
    0x23,0x08, // prelude
    0x16,0x1d,0x1e,0x1f, // names: ioctl, self, req, flags
     // code info
    0xb1, // LOAD_FAST 1
    0x83, // LOAD_CONST_SMALL_INT 3
    0xd9, // BINARY_OP 2 __eq__
    0x44,0x46, // POP_JUMP_IF_FALSE 6
    0xb0, // LOAD_FAST 0
    0x13,0x09, // LOAD_ATTR 'state'
    0xb2, // LOAD_FAST 2
    0xf4, // BINARY_OP 29 __mul__
    0x63, // RETURN_VALUE
    0x7f, // LOAD_CONST_SMALL_INT -1
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_event_ThreadSafeFlag_ioctl = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_event_ThreadSafeFlag_ioctl,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 19,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 5,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 3,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 22,
        .line_info = fun_data_asyncio_event_ThreadSafeFlag_ioctl + 6,
        .line_info_top = fun_data_asyncio_event_ThreadSafeFlag_ioctl + 6,
        .opcodes = fun_data_asyncio_event_ThreadSafeFlag_ioctl + 6,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_event_ThreadSafeFlag_ioctl fun_data_asyncio_event_ThreadSafeFlag_ioctl[0]
#endif

// child of asyncio_event_ThreadSafeFlag
// frozen bytecode for file asyncio/event.py, scope asyncio_event_ThreadSafeFlag_set
static const byte fun_data_asyncio_event_ThreadSafeFlag_set[10] = {
    0x11,0x04, // prelude
    0x0d,0x1d, // names: set, self
     // code info
    0x81, // LOAD_CONST_SMALL_INT 1
    0xb0, // LOAD_FAST 0
    0x18,0x09, // STORE_ATTR 'state'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_event_ThreadSafeFlag_set = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_event_ThreadSafeFlag_set,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 10,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 3,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 13,
        .line_info = fun_data_asyncio_event_ThreadSafeFlag_set + 4,
        .line_info_top = fun_data_asyncio_event_ThreadSafeFlag_set + 4,
        .opcodes = fun_data_asyncio_event_ThreadSafeFlag_set + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_event_ThreadSafeFlag_set fun_data_asyncio_event_ThreadSafeFlag_set[0]
#endif

// child of asyncio_event_ThreadSafeFlag
// frozen bytecode for file asyncio/event.py, scope asyncio_event_ThreadSafeFlag_clear
static const byte fun_data_asyncio_event_ThreadSafeFlag_clear[10] = {
    0x11,0x04, // prelude
    0x12,0x1d, // names: clear, self
     // code info
    0x80, // LOAD_CONST_SMALL_INT 0
    0xb0, // LOAD_FAST 0
    0x18,0x09, // STORE_ATTR 'state'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_event_ThreadSafeFlag_clear = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_event_ThreadSafeFlag_clear,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 10,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 3,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 18,
        .line_info = fun_data_asyncio_event_ThreadSafeFlag_clear + 4,
        .line_info_top = fun_data_asyncio_event_ThreadSafeFlag_clear + 4,
        .opcodes = fun_data_asyncio_event_ThreadSafeFlag_clear + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_event_ThreadSafeFlag_clear fun_data_asyncio_event_ThreadSafeFlag_clear[0]
#endif

// child of asyncio_event_ThreadSafeFlag
// frozen bytecode for file asyncio/event.py, scope asyncio_event_ThreadSafeFlag_wait
static const byte fun_data_asyncio_event_ThreadSafeFlag_wait[27] = {
    0x99,0x40,0x04, // prelude
    0x13,0x1d, // names: wait, self
     // code info
    0xb0, // LOAD_FAST 0
    0x13,0x09, // LOAD_ATTR 'state'
    0x43,0x4b, // POP_JUMP_IF_TRUE 11
    0x12,0x02, // LOAD_GLOBAL 'core'
    0x13,0x17, // LOAD_ATTR '_io_queue'
    0x14,0x18, // LOAD_METHOD 'queue_read'
    0xb0, // LOAD_FAST 0
    0x36,0x01, // CALL_METHOD 1
    0x67, // YIELD_VALUE
    0x59, // POP_TOP
    0x80, // LOAD_CONST_SMALL_INT 0
    0xb0, // LOAD_FAST 0
    0x18,0x09, // STORE_ATTR 'state'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_event_ThreadSafeFlag_wait = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 1,
    .fun_data = fun_data_asyncio_event_ThreadSafeFlag_wait,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 27,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 4,
        .n_exc_stack = 0,
        .scope_flags = 1,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 19,
        .line_info = fun_data_asyncio_event_ThreadSafeFlag_wait + 5,
        .line_info_top = fun_data_asyncio_event_ThreadSafeFlag_wait + 5,
        .opcodes = fun_data_asyncio_event_ThreadSafeFlag_wait + 5,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_event_ThreadSafeFlag_wait fun_data_asyncio_event_ThreadSafeFlag_wait[0]
#endif

static const mp_raw_code_t *const children_asyncio_event_ThreadSafeFlag[] = {
    (const mp_raw_code_t *)&proto_fun_asyncio_event_ThreadSafeFlag___init__,
    (const mp_raw_code_t *)&proto_fun_asyncio_event_ThreadSafeFlag_ioctl,
    (const mp_raw_code_t *)&proto_fun_asyncio_event_ThreadSafeFlag_set,
    (const mp_raw_code_t *)&proto_fun_asyncio_event_ThreadSafeFlag_clear,
    (const mp_raw_code_t *)&proto_fun_asyncio_event_ThreadSafeFlag_wait,
};

static const mp_raw_code_truncated_t proto_fun_asyncio_event_ThreadSafeFlag = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_event_ThreadSafeFlag,
    .children = (void *)&children_asyncio_event_ThreadSafeFlag,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 33,
    .n_children = 5,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 1,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 0,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 6,
        .line_info = fun_data_asyncio_event_ThreadSafeFlag + 3,
        .line_info_top = fun_data_asyncio_event_ThreadSafeFlag + 3,
        .opcodes = fun_data_asyncio_event_ThreadSafeFlag + 3,
    },
    #endif
    #endif
};

static const mp_raw_code_t *const children_asyncio_event__lt_module_gt_[] = {
    (const mp_raw_code_t *)&proto_fun_asyncio_event_Event,
    (const mp_raw_code_t *)&proto_fun_asyncio_event_ThreadSafeFlag,
};

static const mp_raw_code_truncated_t proto_fun_asyncio_event__lt_module_gt_ = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_event__lt_module_gt_,
    .children = (void *)&children_asyncio_event__lt_module_gt_,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 59,
    .n_children = 2,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 6,
        .n_exc_stack = 1,
        .scope_flags = 0,
        .n_pos_args = 0,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 1,
        .line_info = fun_data_asyncio_event__lt_module_gt_ + 3,
        .line_info_top = fun_data_asyncio_event__lt_module_gt_ + 3,
        .opcodes = fun_data_asyncio_event__lt_module_gt_ + 3,
    },
    #endif
    #endif
};

static const qstr_short_t const_qstr_table_data_asyncio_event[32] = {
    MP_QSTR_asyncio_slash_event_dot_py,
    MP_QSTR__lt_module_gt_,
    MP_QSTR_core,
    MP_QSTR_,
    MP_QSTR_Event,
    MP_QSTR_io,
    MP_QSTR_ThreadSafeFlag,
    MP_QSTR_IOBase,
    MP_QSTR___init__,
    MP_QSTR_state,
    MP_QSTR_TaskQueue,
    MP_QSTR_waiting,
    MP_QSTR_is_set,
    MP_QSTR_set,
    MP_QSTR__task_queue,
    MP_QSTR_push,
    MP_QSTR_pop,
    MP_QSTR_peek,
    MP_QSTR_clear,
    MP_QSTR_wait,
    MP_QSTR_cur_task,
    MP_QSTR_data,
    MP_QSTR_ioctl,
    MP_QSTR__io_queue,
    MP_QSTR_queue_read,
    MP_QSTR_ImportError,
    MP_QSTR___name__,
    MP_QSTR___module__,
    MP_QSTR___qualname__,
    MP_QSTR_self,
    MP_QSTR_req,
    MP_QSTR_flags,
};

static const mp_frozen_module_t frozen_module_asyncio_event = {
    .constants = {
        .qstr_table = (qstr_short_t *)&const_qstr_table_data_asyncio_event,
        .obj_table = NULL,
    },
    .proto_fun = &proto_fun_asyncio_event__lt_module_gt_,
};

////////////////////////////////////////////////////////////////////////////////
// frozen module asyncio_funcs
// - original source file: build-standard/frozen_mpy/asyncio/funcs.mpy
// - frozen file name: asyncio/funcs.py
// - .mpy header: 4d:06:00:1f

// frozen bytecode for file asyncio/funcs.py, scope asyncio_funcs__lt_module_gt_
static const byte fun_data_asyncio_funcs__lt_module_gt_[56] = {
    0x18,0x02, // prelude
    0x01, // names: <module>
     // code info
    0x81, // LOAD_CONST_SMALL_INT 1
    0x10,0x02, // LOAD_CONST_STRING 'core'
    0x2a,0x01, // BUILD_TUPLE 1
    0x1b,0x03, // IMPORT_NAME ''
    0x1c,0x02, // IMPORT_FROM 'core'
    0x16,0x02, // STORE_NAME 'core'
    0x59, // POP_TOP
    0x32,0x00, // MAKE_FUNCTION 0
    0x16,0x07, // STORE_NAME '_run'
    0x11,0x02, // LOAD_NAME 'core'
    0x13,0x04, // LOAD_ATTR 'sleep'
    0x2a,0x01, // BUILD_TUPLE 1
    0x53, // LOAD_NULL
    0x33,0x01, // MAKE_FUNCTION_DEFARGS 1
    0x16,0x0b, // STORE_NAME 'wait_for'
    0x32,0x02, // MAKE_FUNCTION 2
    0x16,0x12, // STORE_NAME 'wait_for_ms'
    0x54, // LOAD_BUILD_CLASS
    0x32,0x03, // MAKE_FUNCTION 3
    0x10,0x05, // LOAD_CONST_STRING '_Remove'
    0x34,0x02, // CALL_FUNCTION 2
    0x16,0x05, // STORE_NAME '_Remove'
    0x53, // LOAD_NULL
    0x2c,0x00, // BUILD_MAP 0
    0x50, // LOAD_CONST_FALSE
    0x10,0x06, // LOAD_CONST_STRING 'return_exceptions'
    0x62, // STORE_MAP
    0x33,0x04, // MAKE_FUNCTION_DEFARGS 4
    0x16,0x14, // STORE_NAME 'gather'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
// child of asyncio_funcs__lt_module_gt_
// frozen bytecode for file asyncio/funcs.py, scope asyncio_funcs__run
static const byte fun_data_asyncio_funcs__run[66] = {
    0xd2,0x42,0x06, // prelude
    0x07,0x1b,0x1c, // names: _run, waiter, aw
     // code info
    0x48,0x09, // SETUP_EXCEPT 9
    0xb1, // LOAD_FAST 1
    0x5e, // GET_ITER
    0x51, // LOAD_CONST_NONE
    0x68, // YIELD_FROM
    0xc2, // STORE_FAST 2
    0x52, // LOAD_CONST_TRUE
    0xc3, // STORE_FAST 3
    0x4a,0x16, // POP_EXCEPT_JUMP 22
    0x57, // DUP_TOP
    0x12,0x1d, // LOAD_GLOBAL 'BaseException'
    0xdf, // BINARY_OP 8 <exception match>
    0x44,0x4f, // POP_JUMP_IF_FALSE 15
    0xc4, // STORE_FAST 4
    0x49,0x05, // SETUP_FINALLY 5
    0x51, // LOAD_CONST_NONE
    0xc2, // STORE_FAST 2
    0xb4, // LOAD_FAST 4
    0xc3, // STORE_FAST 3
    0x51, // LOAD_CONST_NONE
    0x51, // LOAD_CONST_NONE
    0xc4, // STORE_FAST 4
    0x28,0x04, // DELETE_FAST 4
    0x5d, // END_FINALLY
    0x4a,0x01, // POP_EXCEPT_JUMP 1
    0x5d, // END_FINALLY
    0xb0, // LOAD_FAST 0
    0x13,0x08, // LOAD_ATTR 'data'
    0x51, // LOAD_CONST_NONE
    0xde, // BINARY_OP 7 <is>
    0x44,0x52, // POP_JUMP_IF_FALSE 18
    0xb0, // LOAD_FAST 0
    0x14,0x09, // LOAD_METHOD 'cancel'
    0x36,0x00, // CALL_METHOD 0
    0x44,0x4b, // POP_JUMP_IF_FALSE 11
    0x12,0x02, // LOAD_GLOBAL 'core'
    0x14,0x0a, // LOAD_METHOD 'CancelledError'
    0xb3, // LOAD_FAST 3
    0xb2, // LOAD_FAST 2
    0x36,0x02, // CALL_METHOD 2
    0xb0, // LOAD_FAST 0
    0x18,0x08, // STORE_ATTR 'data'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_funcs__run = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 1,
    .fun_data = fun_data_asyncio_funcs__run,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 66,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 11,
        .n_exc_stack = 2,
        .scope_flags = 1,
        .n_pos_args = 2,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 7,
        .line_info = fun_data_asyncio_funcs__run + 6,
        .line_info_top = fun_data_asyncio_funcs__run + 6,
        .opcodes = fun_data_asyncio_funcs__run + 6,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_funcs__run fun_data_asyncio_funcs__run[0]
#endif

// child of asyncio_funcs__lt_module_gt_
// frozen bytecode for file asyncio/funcs.py, scope asyncio_funcs_wait_for
static const byte fun_data_asyncio_funcs_wait_for[119] = {
    0xdb,0x43,0x08, // prelude
    0x0b,0x1c,0x1e,0x04, // names: wait_for, aw, timeout, sleep
     // code info
    0x12,0x02, // LOAD_GLOBAL 'core'
    0x14,0x0c, // LOAD_METHOD '_promote_to_task'
    0xb0, // LOAD_FAST 0
    0x36,0x01, // CALL_METHOD 1
    0xc0, // STORE_FAST 0
    0xb1, // LOAD_FAST 1
    0x51, // LOAD_CONST_NONE
    0xde, // BINARY_OP 7 <is>
    0x44,0x45, // POP_JUMP_IF_FALSE 5
    0xb0, // LOAD_FAST 0
    0x5e, // GET_ITER
    0x51, // LOAD_CONST_NONE
    0x68, // YIELD_FROM
    0x63, // RETURN_VALUE
    0x12,0x02, // LOAD_GLOBAL 'core'
    0x14,0x0d, // LOAD_METHOD 'create_task'
    0x12,0x07, // LOAD_GLOBAL '_run'
    0x12,0x02, // LOAD_GLOBAL 'core'
    0x13,0x0e, // LOAD_ATTR 'cur_task'
    0xb0, // LOAD_FAST 0
    0x34,0x02, // CALL_FUNCTION 2
    0x36,0x01, // CALL_METHOD 1
    0xc3, // STORE_FAST 3
    0x48,0x0a, // SETUP_EXCEPT 10
    0xb2, // LOAD_FAST 2
    0xb1, // LOAD_FAST 1
    0x34,0x01, // CALL_FUNCTION 1
    0x5e, // GET_ITER
    0x51, // LOAD_CONST_NONE
    0x68, // YIELD_FROM
    0x59, // POP_TOP
    0x4a,0x32, // POP_EXCEPT_JUMP 50
    0x57, // DUP_TOP
    0x12,0x02, // LOAD_GLOBAL 'core'
    0x13,0x0a, // LOAD_ATTR 'CancelledError'
    0xdf, // BINARY_OP 8 <exception match>
    0x44,0x69, // POP_JUMP_IF_FALSE 41
    0xc4, // STORE_FAST 4
    0x49,0x1f, // SETUP_FINALLY 31
    0xb4, // LOAD_FAST 4
    0x13,0x0f, // LOAD_ATTR 'value'
    0xc5, // STORE_FAST 5
    0xb5, // LOAD_FAST 5
    0x51, // LOAD_CONST_NONE
    0xde, // BINARY_OP 7 <is>
    0x44,0x48, // POP_JUMP_IF_FALSE 8
    0xb3, // LOAD_FAST 3
    0x14,0x09, // LOAD_METHOD 'cancel'
    0x36,0x00, // CALL_METHOD 0
    0x59, // POP_TOP
    0xb4, // LOAD_FAST 4
    0x65, // RAISE_OBJ
    0xb5, // LOAD_FAST 5
    0x52, // LOAD_CONST_TRUE
    0xde, // BINARY_OP 7 <is>
    0x44,0x46, // POP_JUMP_IF_FALSE 6
    0xb4, // LOAD_FAST 4
    0x13,0x10, // LOAD_ATTR 'args'
    0x81, // LOAD_CONST_SMALL_INT 1
    0x55, // LOAD_SUBSCR
    0x63, // RETURN_VALUE
    0xb5, // LOAD_FAST 5
    0x65, // RAISE_OBJ
    0x51, // LOAD_CONST_NONE
    0x51, // LOAD_CONST_NONE
    0xc4, // STORE_FAST 4
    0x28,0x04, // DELETE_FAST 4
    0x5d, // END_FINALLY
    0x4a,0x01, // POP_EXCEPT_JUMP 1
    0x5d, // END_FINALLY
    0xb3, // LOAD_FAST 3
    0x14,0x09, // LOAD_METHOD 'cancel'
    0x36,0x00, // CALL_METHOD 0
    0x59, // POP_TOP
    0xb3, // LOAD_FAST 3
    0x5e, // GET_ITER
    0x51, // LOAD_CONST_NONE
    0x68, // YIELD_FROM
    0x59, // POP_TOP
    0x12,0x02, // LOAD_GLOBAL 'core'
    0x13,0x11, // LOAD_ATTR 'TimeoutError'
    0x65, // RAISE_OBJ
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_funcs_wait_for = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 1,
    .fun_data = fun_data_asyncio_funcs_wait_for,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 119,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 12,
        .n_exc_stack = 2,
        .scope_flags = 1,
        .n_pos_args = 3,
        .n_kwonly_args = 0,
        .n_def_pos_args = 1,
        .qstr_block_name_idx = 11,
        .line_info = fun_data_asyncio_funcs_wait_for + 7,
        .line_info_top = fun_data_asyncio_funcs_wait_for + 7,
        .opcodes = fun_data_asyncio_funcs_wait_for + 7,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_funcs_wait_for fun_data_asyncio_funcs_wait_for[0]
#endif

// child of asyncio_funcs__lt_module_gt_
// frozen bytecode for file asyncio/funcs.py, scope asyncio_funcs_wait_for_ms
static const byte fun_data_asyncio_funcs_wait_for_ms[16] = {
    0x2a,0x06, // prelude
    0x12,0x1c,0x1e, // names: wait_for_ms, aw, timeout
     // code info
    0x12,0x0b, // LOAD_GLOBAL 'wait_for'
    0xb0, // LOAD_FAST 0
    0xb1, // LOAD_FAST 1
    0x12,0x02, // LOAD_GLOBAL 'core'
    0x13,0x13, // LOAD_ATTR 'sleep_ms'
    0x34,0x03, // CALL_FUNCTION 3
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_funcs_wait_for_ms = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_funcs_wait_for_ms,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 16,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 6,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 2,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 18,
        .line_info = fun_data_asyncio_funcs_wait_for_ms + 5,
        .line_info_top = fun_data_asyncio_funcs_wait_for_ms + 5,
        .opcodes = fun_data_asyncio_funcs_wait_for_ms + 5,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_funcs_wait_for_ms fun_data_asyncio_funcs_wait_for_ms[0]
#endif

// child of asyncio_funcs__lt_module_gt_
// frozen bytecode for file asyncio/funcs.py, scope asyncio_funcs__Remove
static const byte fun_data_asyncio_funcs__Remove[21] = {
    0x08,0x02, // prelude
    0x05, // names: _Remove
     // code info
    0x11,0x1f, // LOAD_NAME '__name__'
    0x16,0x20, // STORE_NAME '__module__'
    0x10,0x05, // LOAD_CONST_STRING '_Remove'
    0x16,0x21, // STORE_NAME '__qualname__'
    0x11,0x22, // LOAD_NAME 'staticmethod'
    0x32,0x00, // MAKE_FUNCTION 0
    0x34,0x01, // CALL_FUNCTION 1
    0x16,0x16, // STORE_NAME 'remove'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
// child of asyncio_funcs__Remove
// frozen bytecode for file asyncio/funcs.py, scope asyncio_funcs__Remove_remove
static const byte fun_data_asyncio_funcs__Remove_remove[6] = {
    0x09,0x04, // prelude
    0x16,0x28, // names: remove, t
     // code info
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_funcs__Remove_remove = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_funcs__Remove_remove,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 6,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 2,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 22,
        .line_info = fun_data_asyncio_funcs__Remove_remove + 4,
        .line_info_top = fun_data_asyncio_funcs__Remove_remove + 4,
        .opcodes = fun_data_asyncio_funcs__Remove_remove + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_funcs__Remove_remove fun_data_asyncio_funcs__Remove_remove[0]
#endif

static const mp_raw_code_t *const children_asyncio_funcs__Remove[] = {
    (const mp_raw_code_t *)&proto_fun_asyncio_funcs__Remove_remove,
};

static const mp_raw_code_truncated_t proto_fun_asyncio_funcs__Remove = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_funcs__Remove,
    .children = (void *)&children_asyncio_funcs__Remove,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 21,
    .n_children = 1,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 2,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 0,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 5,
        .line_info = fun_data_asyncio_funcs__Remove + 3,
        .line_info_top = fun_data_asyncio_funcs__Remove + 3,
        .opcodes = fun_data_asyncio_funcs__Remove + 3,
    },
    #endif
    #endif
};

// child of asyncio_funcs__lt_module_gt_
// frozen bytecode for file asyncio/funcs.py, scope asyncio_funcs_gather
static const byte fun_data_asyncio_funcs_gather[281] = {
    0xf0,0xca,0x80,0xc0,0x40,0x85,0x01, // prelude
    0x14,0x06, // names: gather, return_exceptions
    0x00,0x07,0x08, // code info
    0xb0, // LOAD_FAST 0
    0xb7, // LOAD_FAST 7
    0xb8, // LOAD_FAST 8
    0x20,0x00,0x03, // MAKE_CLOSURE 0
    0xc2, // STORE_FAST 2
    0x32,0x01, // MAKE_FUNCTION 1
    0xb1, // LOAD_FAST 1
    0x34,0x01, // CALL_FUNCTION 1
    0xc3, // STORE_FAST 3
    0x80, // LOAD_CONST_SMALL_INT 0
    0x27,0x07, // STORE_DEREF 7
    0x12,0x23, // LOAD_GLOBAL 'len'
    0xb3, // LOAD_FAST 3
    0x34,0x01, // CALL_FUNCTION 1
    0x80, // LOAD_CONST_SMALL_INT 0
    0x42,0xc4,0x80, // JUMP 68
    0x57, // DUP_TOP
    0xc4, // STORE_FAST 4
    0xb3, // LOAD_FAST 3
    0xb4, // LOAD_FAST 4
    0x55, // LOAD_SUBSCR
    0x13,0x15, // LOAD_ATTR 'state'
    0x52, // LOAD_CONST_TRUE
    0xde, // BINARY_OP 7 <is>
    0x44,0x4e, // POP_JUMP_IF_FALSE 14
    0xb2, // LOAD_FAST 2
    0xb3, // LOAD_FAST 3
    0xb4, // LOAD_FAST 4
    0x55, // LOAD_SUBSCR
    0x18,0x15, // STORE_ATTR 'state'
    0x25,0x07, // LOAD_DEREF 7
    0x81, // LOAD_CONST_SMALL_INT 1
    0xe5, // BINARY_OP 14 __iadd__
    0x27,0x07, // STORE_DEREF 7
    0x42,0x69, // JUMP 41
    0xb3, // LOAD_FAST 3
    0xb4, // LOAD_FAST 4
    0x55, // LOAD_SUBSCR
    0x13,0x15, // LOAD_ATTR 'state'
    0x43,0x5b, // POP_JUMP_IF_TRUE 27
    0x12,0x24, // LOAD_GLOBAL 'isinstance'
    0xb3, // LOAD_FAST 3
    0xb4, // LOAD_FAST 4
    0x55, // LOAD_SUBSCR
    0x13,0x08, // LOAD_ATTR 'data'
    0x12,0x25, // LOAD_GLOBAL 'StopIteration'
    0x34,0x02, // CALL_FUNCTION 2
    0x43,0x4c, // POP_JUMP_IF_TRUE 12
    0x25,0x00, // LOAD_DEREF 0
    0x43,0x48, // POP_JUMP_IF_TRUE 8
    0x12,0x23, // LOAD_GLOBAL 'len'
    0xb3, // LOAD_FAST 3
    0x34,0x01, // CALL_FUNCTION 1
    0xd1, // UNARY_OP 1 __neg__
    0x27,0x07, // STORE_DEREF 7
    0x42,0x47, // JUMP 7
    0x12,0x26, // LOAD_GLOBAL 'RuntimeError'
    0x23,0x00, // LOAD_CONST_OBJ 0
    0x34,0x01, // CALL_FUNCTION 1
    0x65, // RAISE_OBJ
    0x81, // LOAD_CONST_SMALL_INT 1
    0xe5, // BINARY_OP 14 __iadd__
    0x58, // DUP_TOP_TWO
    0x5a, // ROT_TWO
    0xd7, // BINARY_OP 0 __lt__
    0x43,0xb6,0x7f, // POP_JUMP_IF_TRUE -74
    0x59, // POP_TOP
    0x59, // POP_TOP
    0x12,0x02, // LOAD_GLOBAL 'core'
    0x13,0x0e, // LOAD_ATTR 'cur_task'
    0x27,0x08, // STORE_DEREF 8
    0x50, // LOAD_CONST_FALSE
    0xc5, // STORE_FAST 5
    0x25,0x07, // LOAD_DEREF 7
    0x80, // LOAD_CONST_SMALL_INT 0
    0xd8, // BINARY_OP 1 __gt__
    0x44,0x66, // POP_JUMP_IF_FALSE 38
    0x12,0x05, // LOAD_GLOBAL '_Remove'
    0x25,0x08, // LOAD_DEREF 8
    0x18,0x08, // STORE_ATTR 'data'
    0x48,0x05, // SETUP_EXCEPT 5
    0x51, // LOAD_CONST_NONE
    0x67, // YIELD_VALUE
    0x59, // POP_TOP
    0x4a,0x19, // POP_EXCEPT_JUMP 25
    0x57, // DUP_TOP
    0x12,0x02, // LOAD_GLOBAL 'core'
    0x13,0x0a, // LOAD_ATTR 'CancelledError'
    0xdf, // BINARY_OP 8 <exception match>
    0x44,0x50, // POP_JUMP_IF_FALSE 16
    0xc6, // STORE_FAST 6
    0x49,0x06, // SETUP_FINALLY 6
    0x52, // LOAD_CONST_TRUE
    0xc5, // STORE_FAST 5
    0xb6, // LOAD_FAST 6
    0x27,0x07, // STORE_DEREF 7
    0x51, // LOAD_CONST_NONE
    0x51, // LOAD_CONST_NONE
    0xc6, // STORE_FAST 6
    0x28,0x06, // DELETE_FAST 6
    0x5d, // END_FINALLY
    0x4a,0x01, // POP_EXCEPT_JUMP 1
    0x5d, // END_FINALLY
    0x12,0x23, // LOAD_GLOBAL 'len'
    0xb3, // LOAD_FAST 3
    0x34,0x01, // CALL_FUNCTION 1
    0x80, // LOAD_CONST_SMALL_INT 0
    0x42,0xda,0x80, // JUMP 90
    0x57, // DUP_TOP
    0xc4, // STORE_FAST 4
    0xb3, // LOAD_FAST 3
    0xb4, // LOAD_FAST 4
    0x55, // LOAD_SUBSCR
    0x13,0x15, // LOAD_ATTR 'state'
    0xb2, // LOAD_FAST 2
    0xde, // BINARY_OP 7 <is>
    0x44,0x53, // POP_JUMP_IF_FALSE 19
    0x52, // LOAD_CONST_TRUE
    0xb3, // LOAD_FAST 3
    0xb4, // LOAD_FAST 4
    0x55, // LOAD_SUBSCR
    0x18,0x15, // STORE_ATTR 'state'
    0xb5, // LOAD_FAST 5
    0x44,0x48, // POP_JUMP_IF_FALSE 8
    0xb3, // LOAD_FAST 3
    0xb4, // LOAD_FAST 4
    0x55, // LOAD_SUBSCR
    0x14,0x09, // LOAD_METHOD 'cancel'
    0x36,0x00, // CALL_METHOD 0
    0x59, // POP_TOP
    0x42,0x7a, // JUMP 58
    0x12,0x24, // LOAD_GLOBAL 'isinstance'
    0xb3, // LOAD_FAST 3
    0xb4, // LOAD_FAST 4
    0x55, // LOAD_SUBSCR
    0x13,0x08, // LOAD_ATTR 'data'
    0x12,0x25, // LOAD_GLOBAL 'StopIteration'
    0x34,0x02, // CALL_FUNCTION 2
    0x44,0x4c, // POP_JUMP_IF_FALSE 12
    0xb3, // LOAD_FAST 3
    0xb4, // LOAD_FAST 4
    0x55, // LOAD_SUBSCR
    0x13,0x08, // LOAD_ATTR 'data'
    0x13,0x0f, // LOAD_ATTR 'value'
    0xb3, // LOAD_FAST 3
    0xb4, // LOAD_FAST 4
    0x56, // STORE_SUBSCR
    0x42,0x61, // JUMP 33
    0x25,0x00, // LOAD_DEREF 0
    0x44,0x4a, // POP_JUMP_IF_FALSE 10
    0xb3, // LOAD_FAST 3
    0xb4, // LOAD_FAST 4
    0x55, // LOAD_SUBSCR
    0x13,0x08, // LOAD_ATTR 'data'
    0xb3, // LOAD_FAST 3
    0xb4, // LOAD_FAST 4
    0x56, // STORE_SUBSCR
    0x42,0x53, // JUMP 19
    0x12,0x24, // LOAD_GLOBAL 'isinstance'
    0x25,0x07, // LOAD_DEREF 7
    0x12,0x27, // LOAD_GLOBAL 'int'
    0x34,0x02, // CALL_FUNCTION 2
    0x44,0x49, // POP_JUMP_IF_FALSE 9
    0xb3, // LOAD_FAST 3
    0xb4, // LOAD_FAST 4
    0x55, // LOAD_SUBSCR
    0x13,0x08, // LOAD_ATTR 'data'
    0x27,0x07, // STORE_DEREF 7
    0x42,0x40, // JUMP 0
    0x81, // LOAD_CONST_SMALL_INT 1
    0xe5, // BINARY_OP 14 __iadd__
    0x58, // DUP_TOP_TWO
    0x5a, // ROT_TWO
    0xd7, // BINARY_OP 0 __lt__
    0x43,0xa0,0x7f, // POP_JUMP_IF_TRUE -96
    0x59, // POP_TOP
    0x59, // POP_TOP
    0x25,0x07, // LOAD_DEREF 7
    0x44,0x43, // POP_JUMP_IF_FALSE 3
    0x25,0x07, // LOAD_DEREF 7
    0x65, // RAISE_OBJ
    0xb3, // LOAD_FAST 3
    0x63, // RETURN_VALUE
};
// child of asyncio_funcs_gather
// frozen bytecode for file asyncio/funcs.py, scope asyncio_funcs_gather_done
static const byte fun_data_asyncio_funcs_gather_done[64] = {
    0xb9,0x04,0x0c, // prelude
    0x17,0x29,0x29,0x29,0x28,0x2a, // names: done, *, *, *, t, er
     // code info
    0x25,0x02, // LOAD_DEREF 2
    0x13,0x08, // LOAD_ATTR 'data'
    0x12,0x05, // LOAD_GLOBAL '_Remove'
    0xde, // BINARY_OP 7 <is>
    0xd3, // UNARY_OP 3 <not>
    0x44,0x42, // POP_JUMP_IF_FALSE 2
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
    0x25,0x00, // LOAD_DEREF 0
    0x43,0x4e, // POP_JUMP_IF_TRUE 14
    0x12,0x24, // LOAD_GLOBAL 'isinstance'
    0xb4, // LOAD_FAST 4
    0x12,0x25, // LOAD_GLOBAL 'StopIteration'
    0x34,0x02, // CALL_FUNCTION 2
    0x43,0x45, // POP_JUMP_IF_TRUE 5
    0xb4, // LOAD_FAST 4
    0x27,0x01, // STORE_DEREF 1
    0x42,0x4c, // JUMP 12
    0x25,0x01, // LOAD_DEREF 1
    0x81, // LOAD_CONST_SMALL_INT 1
    0xe6, // BINARY_OP 15 __isub__
    0x27,0x01, // STORE_DEREF 1
    0x25,0x01, // LOAD_DEREF 1
    0x44,0x42, // POP_JUMP_IF_FALSE 2
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
    0x12,0x02, // LOAD_GLOBAL 'core'
    0x13,0x18, // LOAD_ATTR '_task_queue'
    0x14,0x19, // LOAD_METHOD 'push'
    0x25,0x02, // LOAD_DEREF 2
    0x36,0x01, // CALL_METHOD 1
    0x59, // POP_TOP
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_funcs_gather_done = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_funcs_gather_done,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 64,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 8,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 5,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 23,
        .line_info = fun_data_asyncio_funcs_gather_done + 9,
        .line_info_top = fun_data_asyncio_funcs_gather_done + 9,
        .opcodes = fun_data_asyncio_funcs_gather_done + 9,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_funcs_gather_done fun_data_asyncio_funcs_gather_done[0]
#endif

// child of asyncio_funcs_gather
// frozen bytecode for file asyncio/funcs.py, scope asyncio_funcs_gather__lt_listcomp_gt_
static const byte fun_data_asyncio_funcs_gather__lt_listcomp_gt_[23] = {
    0x49,0x04, // prelude
    0x1a,0x29, // names: <listcomp>, *
     // code info
    0x2b,0x00, // BUILD_LIST 0
    0xb0, // LOAD_FAST 0
    0x5f, // GET_ITER_STACK
    0x4b,0x0c, // FOR_ITER 12
    0xc1, // STORE_FAST 1
    0x12,0x02, // LOAD_GLOBAL 'core'
    0x14,0x0c, // LOAD_METHOD '_promote_to_task'
    0xb1, // LOAD_FAST 1
    0x36,0x01, // CALL_METHOD 1
    0x2f,0x14, // STORE_COMP 20
    0x42,0x32, // JUMP -14
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_funcs_gather__lt_listcomp_gt_ = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_funcs_gather__lt_listcomp_gt_,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 23,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 10,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 26,
        .line_info = fun_data_asyncio_funcs_gather__lt_listcomp_gt_ + 4,
        .line_info_top = fun_data_asyncio_funcs_gather__lt_listcomp_gt_ + 4,
        .opcodes = fun_data_asyncio_funcs_gather__lt_listcomp_gt_ + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_funcs_gather__lt_listcomp_gt_ fun_data_asyncio_funcs_gather__lt_listcomp_gt_[0]
#endif

static const mp_raw_code_t *const children_asyncio_funcs_gather[] = {
    (const mp_raw_code_t *)&proto_fun_asyncio_funcs_gather_done,
    (const mp_raw_code_t *)&proto_fun_asyncio_funcs_gather__lt_listcomp_gt_,
};

static const mp_raw_code_truncated_t proto_fun_asyncio_funcs_gather = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 1,
    .fun_data = fun_data_asyncio_funcs_gather,
    .children = (void *)&children_asyncio_funcs_gather,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 281,
    .n_children = 2,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 15,
        .n_exc_stack = 2,
        .scope_flags = 13,
        .n_pos_args = 0,
        .n_kwonly_args = 1,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 20,
        .line_info = fun_data_asyncio_funcs_gather + 9,
        .line_info_top = fun_data_asyncio_funcs_gather + 9,
        .opcodes = fun_data_asyncio_funcs_gather + 12,
    },
    #endif
    #endif
};

static const mp_raw_code_t *const children_asyncio_funcs__lt_module_gt_[] = {
    (const mp_raw_code_t *)&proto_fun_asyncio_funcs__run,
    (const mp_raw_code_t *)&proto_fun_asyncio_funcs_wait_for,
    (const mp_raw_code_t *)&proto_fun_asyncio_funcs_wait_for_ms,
    (const mp_raw_code_t *)&proto_fun_asyncio_funcs__Remove,
    (const mp_raw_code_t *)&proto_fun_asyncio_funcs_gather,
};

static const mp_raw_code_truncated_t proto_fun_asyncio_funcs__lt_module_gt_ = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_funcs__lt_module_gt_,
    .children = (void *)&children_asyncio_funcs__lt_module_gt_,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 56,
    .n_children = 5,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 4,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 0,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 1,
        .line_info = fun_data_asyncio_funcs__lt_module_gt_ + 3,
        .line_info_top = fun_data_asyncio_funcs__lt_module_gt_ + 3,
        .opcodes = fun_data_asyncio_funcs__lt_module_gt_ + 3,
    },
    #endif
    #endif
};

static const qstr_short_t const_qstr_table_data_asyncio_funcs[43] = {
    MP_QSTR_asyncio_slash_funcs_dot_py,
    MP_QSTR__lt_module_gt_,
    MP_QSTR_core,
    MP_QSTR_,
    MP_QSTR_sleep,
    MP_QSTR__Remove,
    MP_QSTR_return_exceptions,
    MP_QSTR__run,
    MP_QSTR_data,
    MP_QSTR_cancel,
    MP_QSTR_CancelledError,
    MP_QSTR_wait_for,
    MP_QSTR__promote_to_task,
    MP_QSTR_create_task,
    MP_QSTR_cur_task,
    MP_QSTR_value,
    MP_QSTR_args,
    MP_QSTR_TimeoutError,
    MP_QSTR_wait_for_ms,
    MP_QSTR_sleep_ms,
    MP_QSTR_gather,
    MP_QSTR_state,
    MP_QSTR_remove,
    MP_QSTR_done,
    MP_QSTR__task_queue,
    MP_QSTR_push,
    MP_QSTR__lt_listcomp_gt_,
    MP_QSTR_waiter,
    MP_QSTR_aw,
    MP_QSTR_BaseException,
    MP_QSTR_timeout,
    MP_QSTR___name__,
    MP_QSTR___module__,
    MP_QSTR___qualname__,
    MP_QSTR_staticmethod,
    MP_QSTR_len,
    MP_QSTR_isinstance,
    MP_QSTR_StopIteration,
    MP_QSTR_RuntimeError,
    MP_QSTR_int,
    MP_QSTR_t,
    MP_QSTR__star_,
    MP_QSTR_er,
};

// constants

// constant table
static const mp_rom_obj_t const_obj_table_data_asyncio_funcs[1] = {
    MP_ROM_QSTR(MP_QSTR_can_squot_t_space_gather),
};

static const mp_frozen_module_t frozen_module_asyncio_funcs = {
    .constants = {
        .qstr_table = (qstr_short_t *)&const_qstr_table_data_asyncio_funcs,
        .obj_table = (mp_obj_t *)&const_obj_table_data_asyncio_funcs,
    },
    .proto_fun = &proto_fun_asyncio_funcs__lt_module_gt_,
};

////////////////////////////////////////////////////////////////////////////////
// frozen module asyncio_lock
// - original source file: build-standard/frozen_mpy/asyncio/lock.mpy
// - frozen file name: asyncio/lock.py
// - .mpy header: 4d:06:00:1f

// frozen bytecode for file asyncio/lock.py, scope asyncio_lock__lt_module_gt_
static const byte fun_data_asyncio_lock__lt_module_gt_[26] = {
    0x10,0x02, // prelude
    0x01, // names: <module>
     // code info
    0x81, // LOAD_CONST_SMALL_INT 1
    0x10,0x02, // LOAD_CONST_STRING 'core'
    0x2a,0x01, // BUILD_TUPLE 1
    0x1b,0x03, // IMPORT_NAME ''
    0x1c,0x02, // IMPORT_FROM 'core'
    0x16,0x02, // STORE_NAME 'core'
    0x59, // POP_TOP
    0x54, // LOAD_BUILD_CLASS
    0x32,0x00, // MAKE_FUNCTION 0
    0x10,0x04, // LOAD_CONST_STRING 'Lock'
    0x34,0x02, // CALL_FUNCTION 2
    0x16,0x04, // STORE_NAME 'Lock'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
// child of asyncio_lock__lt_module_gt_
// frozen bytecode for file asyncio/lock.py, scope asyncio_lock_Lock
static const byte fun_data_asyncio_lock_Lock[37] = {
    0x00,0x02, // prelude
    0x04, // names: Lock
     // code info
    0x11,0x15, // LOAD_NAME '__name__'
    0x16,0x16, // STORE_NAME '__module__'
    0x10,0x04, // LOAD_CONST_STRING 'Lock'
    0x16,0x17, // STORE_NAME '__qualname__'
    0x32,0x00, // MAKE_FUNCTION 0
    0x16,0x05, // STORE_NAME '__init__'
    0x32,0x01, // MAKE_FUNCTION 1
    0x16,0x09, // STORE_NAME 'locked'
    0x32,0x02, // MAKE_FUNCTION 2
    0x16,0x0a, // STORE_NAME 'release'
    0x32,0x03, // MAKE_FUNCTION 3
    0x16,0x0f, // STORE_NAME 'acquire'
    0x32,0x04, // MAKE_FUNCTION 4
    0x16,0x13, // STORE_NAME '__aenter__'
    0x32,0x05, // MAKE_FUNCTION 5
    0x16,0x14, // STORE_NAME '__aexit__'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
// child of asyncio_lock_Lock
// frozen bytecode for file asyncio/lock.py, scope asyncio_lock_Lock___init__
static const byte fun_data_asyncio_lock_Lock___init__[19] = {
    0x11,0x04, // prelude
    0x05,0x18, // names: __init__, self
     // code info
    0x80, // LOAD_CONST_SMALL_INT 0
    0xb0, // LOAD_FAST 0
    0x18,0x06, // STORE_ATTR 'state'
    0x12,0x02, // LOAD_GLOBAL 'core'
    0x14,0x07, // LOAD_METHOD 'TaskQueue'
    0x36,0x00, // CALL_METHOD 0
    0xb0, // LOAD_FAST 0
    0x18,0x08, // STORE_ATTR 'waiting'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_lock_Lock___init__ = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_lock_Lock___init__,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 19,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 3,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 5,
        .line_info = fun_data_asyncio_lock_Lock___init__ + 4,
        .line_info_top = fun_data_asyncio_lock_Lock___init__ + 4,
        .opcodes = fun_data_asyncio_lock_Lock___init__ + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_lock_Lock___init__ fun_data_asyncio_lock_Lock___init__[0]
#endif

// child of asyncio_lock_Lock
// frozen bytecode for file asyncio/lock.py, scope asyncio_lock_Lock_locked
static const byte fun_data_asyncio_lock_Lock_locked[10] = {
    0x11,0x04, // prelude
    0x09,0x18, // names: locked, self
     // code info
    0xb0, // LOAD_FAST 0
    0x13,0x06, // LOAD_ATTR 'state'
    0x81, // LOAD_CONST_SMALL_INT 1
    0xd9, // BINARY_OP 2 __eq__
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_lock_Lock_locked = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_lock_Lock_locked,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 10,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 3,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 9,
        .line_info = fun_data_asyncio_lock_Lock_locked + 4,
        .line_info_top = fun_data_asyncio_lock_Lock_locked + 4,
        .opcodes = fun_data_asyncio_lock_Lock_locked + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_lock_Lock_locked fun_data_asyncio_lock_Lock_locked[0]
#endif

// child of asyncio_lock_Lock
// frozen bytecode for file asyncio/lock.py, scope asyncio_lock_Lock_release
static const byte fun_data_asyncio_lock_Lock_release[57] = {
    0x19,0x04, // prelude
    0x0a,0x18, // names: release, self
     // code info
    0xb0, // LOAD_FAST 0
    0x13,0x06, // LOAD_ATTR 'state'
    0x81, // LOAD_CONST_SMALL_INT 1
    0xdc, // BINARY_OP 5 __ne__
    0x44,0x47, // POP_JUMP_IF_FALSE 7
    0x12,0x19, // LOAD_GLOBAL 'RuntimeError'
    0x23,0x00, // LOAD_CONST_OBJ 0
    0x34,0x01, // CALL_FUNCTION 1
    0x65, // RAISE_OBJ
    0xb0, // LOAD_FAST 0
    0x13,0x08, // LOAD_ATTR 'waiting'
    0x14,0x0b, // LOAD_METHOD 'peek'
    0x36,0x00, // CALL_METHOD 0
    0x44,0x58, // POP_JUMP_IF_FALSE 24
    0xb0, // LOAD_FAST 0
    0x13,0x08, // LOAD_ATTR 'waiting'
    0x14,0x0c, // LOAD_METHOD 'pop'
    0x36,0x00, // CALL_METHOD 0
    0xb0, // LOAD_FAST 0
    0x18,0x06, // STORE_ATTR 'state'
    0x12,0x02, // LOAD_GLOBAL 'core'
    0x13,0x0d, // LOAD_ATTR '_task_queue'
    0x14,0x0e, // LOAD_METHOD 'push'
    0xb0, // LOAD_FAST 0
    0x13,0x06, // LOAD_ATTR 'state'
    0x36,0x01, // CALL_METHOD 1
    0x59, // POP_TOP
    0x42,0x44, // JUMP 4
    0x80, // LOAD_CONST_SMALL_INT 0
    0xb0, // LOAD_FAST 0
    0x18,0x06, // STORE_ATTR 'state'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_lock_Lock_release = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_lock_Lock_release,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 57,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 4,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 10,
        .line_info = fun_data_asyncio_lock_Lock_release + 4,
        .line_info_top = fun_data_asyncio_lock_Lock_release + 4,
        .opcodes = fun_data_asyncio_lock_Lock_release + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_lock_Lock_release fun_data_asyncio_lock_Lock_release[0]
#endif

// child of asyncio_lock_Lock
// frozen bytecode for file asyncio/lock.py, scope asyncio_lock_Lock_acquire
static const byte fun_data_asyncio_lock_Lock_acquire[88] = {
    0xb9,0x42,0x04, // prelude
    0x0f,0x18, // names: acquire, self
     // code info
    0xb0, // LOAD_FAST 0
    0x13,0x06, // LOAD_ATTR 'state'
    0x80, // LOAD_CONST_SMALL_INT 0
    0xdc, // BINARY_OP 5 __ne__
    0x44,0xc5,0x80, // POP_JUMP_IF_FALSE 69
    0xb0, // LOAD_FAST 0
    0x13,0x08, // LOAD_ATTR 'waiting'
    0x14,0x0e, // LOAD_METHOD 'push'
    0x12,0x02, // LOAD_GLOBAL 'core'
    0x13,0x10, // LOAD_ATTR 'cur_task'
    0x36,0x01, // CALL_METHOD 1
    0x59, // POP_TOP
    0xb0, // LOAD_FAST 0
    0x13,0x08, // LOAD_ATTR 'waiting'
    0x12,0x02, // LOAD_GLOBAL 'core'
    0x13,0x10, // LOAD_ATTR 'cur_task'
    0x18,0x11, // STORE_ATTR 'data'
    0x48,0x05, // SETUP_EXCEPT 5
    0x51, // LOAD_CONST_NONE
    0x67, // YIELD_VALUE
    0x59, // POP_TOP
    0x4a,0x29, // POP_EXCEPT_JUMP 41
    0x57, // DUP_TOP
    0x12,0x02, // LOAD_GLOBAL 'core'
    0x13,0x12, // LOAD_ATTR 'CancelledError'
    0xdf, // BINARY_OP 8 <exception match>
    0x44,0x60, // POP_JUMP_IF_FALSE 32
    0xc1, // STORE_FAST 1
    0x49,0x16, // SETUP_FINALLY 22
    0xb0, // LOAD_FAST 0
    0x13,0x06, // LOAD_ATTR 'state'
    0x12,0x02, // LOAD_GLOBAL 'core'
    0x13,0x10, // LOAD_ATTR 'cur_task'
    0xd9, // BINARY_OP 2 __eq__
    0x44,0x4a, // POP_JUMP_IF_FALSE 10
    0x81, // LOAD_CONST_SMALL_INT 1
    0xb0, // LOAD_FAST 0
    0x18,0x06, // STORE_ATTR 'state'
    0xb0, // LOAD_FAST 0
    0x14,0x0a, // LOAD_METHOD 'release'
    0x36,0x00, // CALL_METHOD 0
    0x59, // POP_TOP
    0xb1, // LOAD_FAST 1
    0x65, // RAISE_OBJ
    0x51, // LOAD_CONST_NONE
    0xc1, // STORE_FAST 1
    0x28,0x01, // DELETE_FAST 1
    0x5d, // END_FINALLY
    0x4a,0x01, // POP_EXCEPT_JUMP 1
    0x5d, // END_FINALLY
    0x81, // LOAD_CONST_SMALL_INT 1
    0xb0, // LOAD_FAST 0
    0x18,0x06, // STORE_ATTR 'state'
    0x52, // LOAD_CONST_TRUE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_lock_Lock_acquire = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 1,
    .fun_data = fun_data_asyncio_lock_Lock_acquire,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 88,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 8,
        .n_exc_stack = 2,
        .scope_flags = 1,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 15,
        .line_info = fun_data_asyncio_lock_Lock_acquire + 5,
        .line_info_top = fun_data_asyncio_lock_Lock_acquire + 5,
        .opcodes = fun_data_asyncio_lock_Lock_acquire + 5,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_lock_Lock_acquire fun_data_asyncio_lock_Lock_acquire[0]
#endif

// child of asyncio_lock_Lock
// frozen bytecode for file asyncio/lock.py, scope asyncio_lock_Lock___aenter__
static const byte fun_data_asyncio_lock_Lock___aenter__[14] = {
    0x91,0x40,0x04, // prelude
    0x13,0x18, // names: __aenter__, self
     // code info
    0xb0, // LOAD_FAST 0
    0x14,0x0f, // LOAD_METHOD 'acquire'
    0x36,0x00, // CALL_METHOD 0
    0x5e, // GET_ITER
    0x51, // LOAD_CONST_NONE
    0x68, // YIELD_FROM
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_lock_Lock___aenter__ = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 1,
    .fun_data = fun_data_asyncio_lock_Lock___aenter__,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 14,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 3,
        .n_exc_stack = 0,
        .scope_flags = 1,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 19,
        .line_info = fun_data_asyncio_lock_Lock___aenter__ + 5,
        .line_info_top = fun_data_asyncio_lock_Lock___aenter__ + 5,
        .opcodes = fun_data_asyncio_lock_Lock___aenter__ + 5,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_lock_Lock___aenter__ fun_data_asyncio_lock_Lock___aenter__[0]
#endif

// child of asyncio_lock_Lock
// frozen bytecode for file asyncio/lock.py, scope asyncio_lock_Lock___aexit__
static const byte fun_data_asyncio_lock_Lock___aexit__[14] = {
    0xa8,0x44,0x0a, // prelude
    0x14,0x18,0x1a,0x1b,0x1c, // names: __aexit__, self, exc_type, exc, tb
     // code info
    0xb0, // LOAD_FAST 0
    0x14,0x0a, // LOAD_METHOD 'release'
    0x36,0x00, // CALL_METHOD 0
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_lock_Lock___aexit__ = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 1,
    .fun_data = fun_data_asyncio_lock_Lock___aexit__,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 14,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 6,
        .n_exc_stack = 0,
        .scope_flags = 1,
        .n_pos_args = 4,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 20,
        .line_info = fun_data_asyncio_lock_Lock___aexit__ + 8,
        .line_info_top = fun_data_asyncio_lock_Lock___aexit__ + 8,
        .opcodes = fun_data_asyncio_lock_Lock___aexit__ + 8,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_lock_Lock___aexit__ fun_data_asyncio_lock_Lock___aexit__[0]
#endif

static const mp_raw_code_t *const children_asyncio_lock_Lock[] = {
    (const mp_raw_code_t *)&proto_fun_asyncio_lock_Lock___init__,
    (const mp_raw_code_t *)&proto_fun_asyncio_lock_Lock_locked,
    (const mp_raw_code_t *)&proto_fun_asyncio_lock_Lock_release,
    (const mp_raw_code_t *)&proto_fun_asyncio_lock_Lock_acquire,
    (const mp_raw_code_t *)&proto_fun_asyncio_lock_Lock___aenter__,
    (const mp_raw_code_t *)&proto_fun_asyncio_lock_Lock___aexit__,
};

static const mp_raw_code_truncated_t proto_fun_asyncio_lock_Lock = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_lock_Lock,
    .children = (void *)&children_asyncio_lock_Lock,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 37,
    .n_children = 6,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 1,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 0,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 4,
        .line_info = fun_data_asyncio_lock_Lock + 3,
        .line_info_top = fun_data_asyncio_lock_Lock + 3,
        .opcodes = fun_data_asyncio_lock_Lock + 3,
    },
    #endif
    #endif
};

static const mp_raw_code_t *const children_asyncio_lock__lt_module_gt_[] = {
    (const mp_raw_code_t *)&proto_fun_asyncio_lock_Lock,
};

static const mp_raw_code_truncated_t proto_fun_asyncio_lock__lt_module_gt_ = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_lock__lt_module_gt_,
    .children = (void *)&children_asyncio_lock__lt_module_gt_,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 26,
    .n_children = 1,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 3,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 0,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 1,
        .line_info = fun_data_asyncio_lock__lt_module_gt_ + 3,
        .line_info_top = fun_data_asyncio_lock__lt_module_gt_ + 3,
        .opcodes = fun_data_asyncio_lock__lt_module_gt_ + 3,
    },
    #endif
    #endif
};

static const qstr_short_t const_qstr_table_data_asyncio_lock[29] = {
    MP_QSTR_asyncio_slash_lock_dot_py,
    MP_QSTR__lt_module_gt_,
    MP_QSTR_core,
    MP_QSTR_,
    MP_QSTR_Lock,
    MP_QSTR___init__,
    MP_QSTR_state,
    MP_QSTR_TaskQueue,
    MP_QSTR_waiting,
    MP_QSTR_locked,
    MP_QSTR_release,
    MP_QSTR_peek,
    MP_QSTR_pop,
    MP_QSTR__task_queue,
    MP_QSTR_push,
    MP_QSTR_acquire,
    MP_QSTR_cur_task,
    MP_QSTR_data,
    MP_QSTR_CancelledError,
    MP_QSTR___aenter__,
    MP_QSTR___aexit__,
    MP_QSTR___name__,
    MP_QSTR___module__,
    MP_QSTR___qualname__,
    MP_QSTR_self,
    MP_QSTR_RuntimeError,
    MP_QSTR_exc_type,
    MP_QSTR_exc,
    MP_QSTR_tb,
};

// constants

// constant table
static const mp_rom_obj_t const_obj_table_data_asyncio_lock[1] = {
    MP_ROM_QSTR(MP_QSTR_Lock_space_not_space_acquired),
};

static const mp_frozen_module_t frozen_module_asyncio_lock = {
    .constants = {
        .qstr_table = (qstr_short_t *)&const_qstr_table_data_asyncio_lock,
        .obj_table = (mp_obj_t *)&const_obj_table_data_asyncio_lock,
    },
    .proto_fun = &proto_fun_asyncio_lock__lt_module_gt_,
};

////////////////////////////////////////////////////////////////////////////////
// frozen module asyncio___init__
// - original source file: build-standard/frozen_mpy/asyncio/__init__.mpy
// - frozen file name: asyncio/__init__.py
// - .mpy header: 4d:06:00:1f

// frozen bytecode for file asyncio/__init__.py, scope asyncio___init____lt_module_gt_
static const byte fun_data_asyncio___init____lt_module_gt_[65] = {
    0x18,0x02, // prelude
    0x01, // names: <module>
     // code info
    0x81, // LOAD_CONST_SMALL_INT 1
    0x10,0x02, // LOAD_CONST_STRING '*'
    0x2a,0x01, // BUILD_TUPLE 1
    0x1b,0x03, // IMPORT_NAME 'core'
    0x69, // IMPORT_STAR
    0x81, // LOAD_CONST_SMALL_INT 1
    0x10,0x04, // LOAD_CONST_STRING 'wait_for'
    0x10,0x05, // LOAD_CONST_STRING 'wait_for_ms'
    0x10,0x06, // LOAD_CONST_STRING 'gather'
    0x2a,0x03, // BUILD_TUPLE 3
    0x1b,0x07, // IMPORT_NAME 'funcs'
    0x1c,0x04, // IMPORT_FROM 'wait_for'
    0x16,0x04, // STORE_NAME 'wait_for'
    0x1c,0x05, // IMPORT_FROM 'wait_for_ms'
    0x16,0x05, // STORE_NAME 'wait_for_ms'
    0x1c,0x06, // IMPORT_FROM 'gather'
    0x16,0x06, // STORE_NAME 'gather'
    0x59, // POP_TOP
    0x81, // LOAD_CONST_SMALL_INT 1
    0x10,0x08, // LOAD_CONST_STRING 'Event'
    0x2a,0x01, // BUILD_TUPLE 1
    0x1b,0x09, // IMPORT_NAME 'event'
    0x1c,0x08, // IMPORT_FROM 'Event'
    0x16,0x08, // STORE_NAME 'Event'
    0x59, // POP_TOP
    0x81, // LOAD_CONST_SMALL_INT 1
    0x10,0x0a, // LOAD_CONST_STRING 'Lock'
    0x2a,0x01, // BUILD_TUPLE 1
    0x1b,0x0b, // IMPORT_NAME 'lock'
    0x1c,0x0a, // IMPORT_FROM 'Lock'
    0x16,0x0a, // STORE_NAME 'Lock'
    0x59, // POP_TOP
    0x23,0x00, // LOAD_CONST_OBJ 0
    0x16,0x0c, // STORE_NAME '__version__'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio___init____lt_module_gt_ = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio___init____lt_module_gt_,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 65,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 4,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 0,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 1,
        .line_info = fun_data_asyncio___init____lt_module_gt_ + 3,
        .line_info_top = fun_data_asyncio___init____lt_module_gt_ + 3,
        .opcodes = fun_data_asyncio___init____lt_module_gt_ + 3,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio___init____lt_module_gt_ fun_data_asyncio___init____lt_module_gt_[0]
#endif

static const qstr_short_t const_qstr_table_data_asyncio___init__[13] = {
    MP_QSTR_asyncio_slash___init___dot_py,
    MP_QSTR__lt_module_gt_,
    MP_QSTR__star_,
    MP_QSTR_core,
    MP_QSTR_wait_for,
    MP_QSTR_wait_for_ms,
    MP_QSTR_gather,
    MP_QSTR_funcs,
    MP_QSTR_Event,
    MP_QSTR_event,
    MP_QSTR_Lock,
    MP_QSTR_lock,
    MP_QSTR___version__,
};

// constants
static const mp_rom_obj_tuple_t const_obj_asyncio___init___0 = {{&mp_type_tuple}, 3, {
    MP_ROM_INT(3),
    MP_ROM_INT(0),
    MP_ROM_INT(0),
}};

// constant table
static const mp_rom_obj_t const_obj_table_data_asyncio___init__[1] = {
    MP_ROM_PTR(&const_obj_asyncio___init___0),
};

static const mp_frozen_module_t frozen_module_asyncio___init__ = {
    .constants = {
        .qstr_table = (qstr_short_t *)&const_qstr_table_data_asyncio___init__,
        .obj_table = (mp_obj_t *)&const_obj_table_data_asyncio___init__,
    },
    .proto_fun = &proto_fun_asyncio___init____lt_module_gt_,
};

////////////////////////////////////////////////////////////////////////////////
// frozen module asyncio_core
// - original source file: build-standard/frozen_mpy/asyncio/core.mpy
// - frozen file name: asyncio/core.py
// - .mpy header: 4d:06:00:1f

// frozen bytecode for file asyncio/core.py, scope asyncio_core__lt_module_gt_
static const byte fun_data_asyncio_core__lt_module_gt_[207] = {
    0x18,0x02, // prelude
    0x01, // names: <module>
     // code info
    0x80, // LOAD_CONST_SMALL_INT 0
    0x10,0x02, // LOAD_CONST_STRING 'ticks_ms'
    0x10,0x03, // LOAD_CONST_STRING 'ticks_diff'
    0x10,0x04, // LOAD_CONST_STRING 'ticks_add'
    0x2a,0x03, // BUILD_TUPLE 3
    0x1b,0x05, // IMPORT_NAME 'time'
    0x1c,0x02, // IMPORT_FROM 'ticks_ms'
    0x16,0x45, // STORE_NAME 'ticks'
    0x1c,0x03, // IMPORT_FROM 'ticks_diff'
    0x16,0x03, // STORE_NAME 'ticks_diff'
    0x1c,0x04, // IMPORT_FROM 'ticks_add'
    0x16,0x04, // STORE_NAME 'ticks_add'
    0x59, // POP_TOP
    0x80, // LOAD_CONST_SMALL_INT 0
    0x51, // LOAD_CONST_NONE
    0x1b,0x06, // IMPORT_NAME 'sys'
    0x16,0x06, // STORE_NAME 'sys'
    0x80, // LOAD_CONST_SMALL_INT 0
    0x51, // LOAD_CONST_NONE
    0x1b,0x07, // IMPORT_NAME 'js'
    0x16,0x07, // STORE_NAME 'js'
    0x80, // LOAD_CONST_SMALL_INT 0
    0x51, // LOAD_CONST_NONE
    0x1b,0x08, // IMPORT_NAME 'jsffi'
    0x16,0x08, // STORE_NAME 'jsffi'
    0x80, // LOAD_CONST_SMALL_INT 0
    0x10,0x09, // LOAD_CONST_STRING 'TaskQueue'
    0x10,0x0a, // LOAD_CONST_STRING 'Task'
    0x2a,0x02, // BUILD_TUPLE 2
    0x1b,0x0b, // IMPORT_NAME '_asyncio'
    0x1c,0x09, // IMPORT_FROM 'TaskQueue'
    0x16,0x09, // STORE_NAME 'TaskQueue'
    0x1c,0x0a, // IMPORT_FROM 'Task'
    0x16,0x0a, // STORE_NAME 'Task'
    0x59, // POP_TOP
    0x54, // LOAD_BUILD_CLASS
    0x32,0x00, // MAKE_FUNCTION 0
    0x10,0x0c, // LOAD_CONST_STRING 'CancelledError'
    0x11,0x46, // LOAD_NAME 'BaseException'
    0x34,0x03, // CALL_FUNCTION 3
    0x16,0x0c, // STORE_NAME 'CancelledError'
    0x54, // LOAD_BUILD_CLASS
    0x32,0x01, // MAKE_FUNCTION 1
    0x10,0x0d, // LOAD_CONST_STRING 'TimeoutError'
    0x11,0x47, // LOAD_NAME 'Exception'
    0x34,0x03, // CALL_FUNCTION 3
    0x16,0x0d, // STORE_NAME 'TimeoutError'
    0x2c,0x03, // BUILD_MAP 3
    0x23,0x00, // LOAD_CONST_OBJ 0
    0x10,0x0e, // LOAD_CONST_STRING 'message'
    0x62, // STORE_MAP
    0x51, // LOAD_CONST_NONE
    0x10,0x0f, // LOAD_CONST_STRING 'exception'
    0x62, // STORE_MAP
    0x51, // LOAD_CONST_NONE
    0x10,0x10, // LOAD_CONST_STRING 'future'
    0x62, // STORE_MAP
    0x16,0x48, // STORE_NAME '_exc_context'
    0x54, // LOAD_BUILD_CLASS
    0x32,0x02, // MAKE_FUNCTION 2
    0x10,0x11, // LOAD_CONST_STRING 'SingletonGenerator'
    0x34,0x02, // CALL_FUNCTION 2
    0x16,0x11, // STORE_NAME 'SingletonGenerator'
    0x11,0x11, // LOAD_NAME 'SingletonGenerator'
    0x34,0x00, // CALL_FUNCTION 0
    0x2a,0x01, // BUILD_TUPLE 1
    0x53, // LOAD_NULL
    0x33,0x03, // MAKE_FUNCTION_DEFARGS 3
    0x16,0x15, // STORE_NAME 'sleep_ms'
    0x32,0x04, // MAKE_FUNCTION 4
    0x16,0x17, // STORE_NAME 'sleep'
    0x51, // LOAD_CONST_NONE
    0x17,0x49, // STORE_GLOBAL 'asyncio_timer'
    0x54, // LOAD_BUILD_CLASS
    0x32,0x05, // MAKE_FUNCTION 5
    0x10,0x12, // LOAD_CONST_STRING 'TopLevelCoro'
    0x34,0x02, // CALL_FUNCTION 2
    0x16,0x12, // STORE_NAME 'TopLevelCoro'
    0x54, // LOAD_BUILD_CLASS
    0x32,0x06, // MAKE_FUNCTION 6
    0x10,0x13, // LOAD_CONST_STRING 'ThenableEvent'
    0x34,0x02, // CALL_FUNCTION 2
    0x16,0x13, // STORE_NAME 'ThenableEvent'
    0x32,0x07, // MAKE_FUNCTION 7
    0x16,0x18, // STORE_NAME '_promote_to_task'
    0x32,0x08, // MAKE_FUNCTION 8
    0x16,0x19, // STORE_NAME '_schedule_run_iter'
    0x32,0x09, // MAKE_FUNCTION 9
    0x16,0x1c, // STORE_NAME '_run_iter'
    0x32,0x0a, // MAKE_FUNCTION 10
    0x16,0x26, // STORE_NAME 'create_task'
    0x11,0x0a, // LOAD_NAME 'Task'
    0x11,0x12, // LOAD_NAME 'TopLevelCoro'
    0x11,0x4a, // LOAD_NAME 'globals'
    0x34,0x00, // CALL_FUNCTION 0
    0x34,0x02, // CALL_FUNCTION 2
    0x16,0x4b, // STORE_NAME '_top_level_task'
    0x11,0x4b, // LOAD_NAME '_top_level_task'
    0x17,0x4c, // STORE_GLOBAL 'cur_task'
    0x54, // LOAD_BUILD_CLASS
    0x32,0x0b, // MAKE_FUNCTION 11
    0x10,0x14, // LOAD_CONST_STRING 'Loop'
    0x34,0x02, // CALL_FUNCTION 2
    0x16,0x14, // STORE_NAME 'Loop'
    0x32,0x0c, // MAKE_FUNCTION 12
    0x16,0x27, // STORE_NAME 'get_event_loop'
    0x32,0x0d, // MAKE_FUNCTION 13
    0x16,0x28, // STORE_NAME 'current_task'
    0x32,0x0e, // MAKE_FUNCTION 14
    0x16,0x29, // STORE_NAME 'new_event_loop'
    0x11,0x29, // LOAD_NAME 'new_event_loop'
    0x34,0x00, // CALL_FUNCTION 0
    0x59, // POP_TOP
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
// child of asyncio_core__lt_module_gt_
// frozen bytecode for file asyncio/core.py, scope asyncio_core_CancelledError
static const byte fun_data_asyncio_core_CancelledError[13] = {
    0x00,0x02, // prelude
    0x0c, // names: CancelledError
     // code info
    0x11,0x4d, // LOAD_NAME '__name__'
    0x16,0x4e, // STORE_NAME '__module__'
    0x10,0x0c, // LOAD_CONST_STRING 'CancelledError'
    0x16,0x4f, // STORE_NAME '__qualname__'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_CancelledError = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_CancelledError,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 13,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 1,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 0,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 12,
        .line_info = fun_data_asyncio_core_CancelledError + 3,
        .line_info_top = fun_data_asyncio_core_CancelledError + 3,
        .opcodes = fun_data_asyncio_core_CancelledError + 3,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_CancelledError fun_data_asyncio_core_CancelledError[0]
#endif

// child of asyncio_core__lt_module_gt_
// frozen bytecode for file asyncio/core.py, scope asyncio_core_TimeoutError
static const byte fun_data_asyncio_core_TimeoutError[13] = {
    0x00,0x02, // prelude
    0x0d, // names: TimeoutError
     // code info
    0x11,0x4d, // LOAD_NAME '__name__'
    0x16,0x4e, // STORE_NAME '__module__'
    0x10,0x0d, // LOAD_CONST_STRING 'TimeoutError'
    0x16,0x4f, // STORE_NAME '__qualname__'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_TimeoutError = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_TimeoutError,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 13,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 1,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 0,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 13,
        .line_info = fun_data_asyncio_core_TimeoutError + 3,
        .line_info_top = fun_data_asyncio_core_TimeoutError + 3,
        .opcodes = fun_data_asyncio_core_TimeoutError + 3,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_TimeoutError fun_data_asyncio_core_TimeoutError[0]
#endif

// child of asyncio_core__lt_module_gt_
// frozen bytecode for file asyncio/core.py, scope asyncio_core_SingletonGenerator
static const byte fun_data_asyncio_core_SingletonGenerator[25] = {
    0x00,0x02, // prelude
    0x11, // names: SingletonGenerator
     // code info
    0x11,0x4d, // LOAD_NAME '__name__'
    0x16,0x4e, // STORE_NAME '__module__'
    0x10,0x11, // LOAD_CONST_STRING 'SingletonGenerator'
    0x16,0x4f, // STORE_NAME '__qualname__'
    0x32,0x00, // MAKE_FUNCTION 0
    0x16,0x2a, // STORE_NAME '__init__'
    0x32,0x01, // MAKE_FUNCTION 1
    0x16,0x2c, // STORE_NAME '__iter__'
    0x32,0x02, // MAKE_FUNCTION 2
    0x16,0x2d, // STORE_NAME '__next__'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
// child of asyncio_core_SingletonGenerator
// frozen bytecode for file asyncio/core.py, scope asyncio_core_SingletonGenerator___init__
static const byte fun_data_asyncio_core_SingletonGenerator___init__[17] = {
    0x11,0x04, // prelude
    0x2a,0x5d, // names: __init__, self
     // code info
    0x51, // LOAD_CONST_NONE
    0xb0, // LOAD_FAST 0
    0x18,0x16, // STORE_ATTR 'state'
    0x12,0x58, // LOAD_GLOBAL 'StopIteration'
    0x34,0x00, // CALL_FUNCTION 0
    0xb0, // LOAD_FAST 0
    0x18,0x2b, // STORE_ATTR 'exc'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_SingletonGenerator___init__ = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_SingletonGenerator___init__,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 17,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 3,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 42,
        .line_info = fun_data_asyncio_core_SingletonGenerator___init__ + 4,
        .line_info_top = fun_data_asyncio_core_SingletonGenerator___init__ + 4,
        .opcodes = fun_data_asyncio_core_SingletonGenerator___init__ + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_SingletonGenerator___init__ fun_data_asyncio_core_SingletonGenerator___init__[0]
#endif

// child of asyncio_core_SingletonGenerator
// frozen bytecode for file asyncio/core.py, scope asyncio_core_SingletonGenerator___iter__
static const byte fun_data_asyncio_core_SingletonGenerator___iter__[6] = {
    0x09,0x04, // prelude
    0x2c,0x5d, // names: __iter__, self
     // code info
    0xb0, // LOAD_FAST 0
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_SingletonGenerator___iter__ = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_SingletonGenerator___iter__,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 6,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 2,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 44,
        .line_info = fun_data_asyncio_core_SingletonGenerator___iter__ + 4,
        .line_info_top = fun_data_asyncio_core_SingletonGenerator___iter__ + 4,
        .opcodes = fun_data_asyncio_core_SingletonGenerator___iter__ + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_SingletonGenerator___iter__ fun_data_asyncio_core_SingletonGenerator___iter__[0]
#endif

// child of asyncio_core_SingletonGenerator
// frozen bytecode for file asyncio/core.py, scope asyncio_core_SingletonGenerator___next__
static const byte fun_data_asyncio_core_SingletonGenerator___next__[42] = {
    0x21,0x04, // prelude
    0x2d,0x5d, // names: __next__, self
     // code info
    0xb0, // LOAD_FAST 0
    0x13,0x16, // LOAD_ATTR 'state'
    0x51, // LOAD_CONST_NONE
    0xde, // BINARY_OP 7 <is>
    0xd3, // UNARY_OP 3 <not>
    0x44,0x52, // POP_JUMP_IF_FALSE 18
    0x12,0x59, // LOAD_GLOBAL '_task_queue'
    0x14,0x24, // LOAD_METHOD 'push'
    0x12,0x4c, // LOAD_GLOBAL 'cur_task'
    0xb0, // LOAD_FAST 0
    0x13,0x16, // LOAD_ATTR 'state'
    0x36,0x02, // CALL_METHOD 2
    0x59, // POP_TOP
    0x51, // LOAD_CONST_NONE
    0xb0, // LOAD_FAST 0
    0x18,0x16, // STORE_ATTR 'state'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
    0x51, // LOAD_CONST_NONE
    0xb0, // LOAD_FAST 0
    0x13,0x2b, // LOAD_ATTR 'exc'
    0x18,0x2e, // STORE_ATTR '__traceback__'
    0xb0, // LOAD_FAST 0
    0x13,0x2b, // LOAD_ATTR 'exc'
    0x65, // RAISE_OBJ
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_SingletonGenerator___next__ = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_SingletonGenerator___next__,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 42,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 5,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 45,
        .line_info = fun_data_asyncio_core_SingletonGenerator___next__ + 4,
        .line_info_top = fun_data_asyncio_core_SingletonGenerator___next__ + 4,
        .opcodes = fun_data_asyncio_core_SingletonGenerator___next__ + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_SingletonGenerator___next__ fun_data_asyncio_core_SingletonGenerator___next__[0]
#endif

static const mp_raw_code_t *const children_asyncio_core_SingletonGenerator[] = {
    (const mp_raw_code_t *)&proto_fun_asyncio_core_SingletonGenerator___init__,
    (const mp_raw_code_t *)&proto_fun_asyncio_core_SingletonGenerator___iter__,
    (const mp_raw_code_t *)&proto_fun_asyncio_core_SingletonGenerator___next__,
};

static const mp_raw_code_truncated_t proto_fun_asyncio_core_SingletonGenerator = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_SingletonGenerator,
    .children = (void *)&children_asyncio_core_SingletonGenerator,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 25,
    .n_children = 3,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 1,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 0,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 17,
        .line_info = fun_data_asyncio_core_SingletonGenerator + 3,
        .line_info_top = fun_data_asyncio_core_SingletonGenerator + 3,
        .opcodes = fun_data_asyncio_core_SingletonGenerator + 3,
    },
    #endif
    #endif
};

// child of asyncio_core__lt_module_gt_
// frozen bytecode for file asyncio/core.py, scope asyncio_core_sleep_ms
static const byte fun_data_asyncio_core_sleep_ms[25] = {
    0xb2,0x01,0x06, // prelude
    0x15,0x50,0x51, // names: sleep_ms, t, sgen
     // code info
    0x12,0x04, // LOAD_GLOBAL 'ticks_add'
    0x12,0x45, // LOAD_GLOBAL 'ticks'
    0x34,0x00, // CALL_FUNCTION 0
    0x12,0x52, // LOAD_GLOBAL 'max'
    0x80, // LOAD_CONST_SMALL_INT 0
    0xb0, // LOAD_FAST 0
    0x34,0x02, // CALL_FUNCTION 2
    0x34,0x02, // CALL_FUNCTION 2
    0xb1, // LOAD_FAST 1
    0x18,0x16, // STORE_ATTR 'state'
    0xb1, // LOAD_FAST 1
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_sleep_ms = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_sleep_ms,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 25,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 7,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 2,
        .n_kwonly_args = 0,
        .n_def_pos_args = 1,
        .qstr_block_name_idx = 21,
        .line_info = fun_data_asyncio_core_sleep_ms + 6,
        .line_info_top = fun_data_asyncio_core_sleep_ms + 6,
        .opcodes = fun_data_asyncio_core_sleep_ms + 6,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_sleep_ms fun_data_asyncio_core_sleep_ms[0]
#endif

// child of asyncio_core__lt_module_gt_
// frozen bytecode for file asyncio/core.py, scope asyncio_core_sleep
static const byte fun_data_asyncio_core_sleep[18] = {
    0x21,0x04, // prelude
    0x17,0x50, // names: sleep, t
     // code info
    0x12,0x15, // LOAD_GLOBAL 'sleep_ms'
    0x12,0x53, // LOAD_GLOBAL 'int'
    0xb0, // LOAD_FAST 0
    0x22,0x87,0x68, // LOAD_CONST_SMALL_INT 1000
    0xf4, // BINARY_OP 29 __mul__
    0x34,0x01, // CALL_FUNCTION 1
    0x34,0x01, // CALL_FUNCTION 1
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_sleep = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_sleep,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 18,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 5,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 23,
        .line_info = fun_data_asyncio_core_sleep + 4,
        .line_info_top = fun_data_asyncio_core_sleep + 4,
        .opcodes = fun_data_asyncio_core_sleep + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_sleep fun_data_asyncio_core_sleep[0]
#endif

// child of asyncio_core__lt_module_gt_
// frozen bytecode for file asyncio/core.py, scope asyncio_core_TopLevelCoro
static const byte fun_data_asyncio_core_TopLevelCoro[29] = {
    0x08,0x02, // prelude
    0x12, // names: TopLevelCoro
     // code info
    0x11,0x4d, // LOAD_NAME '__name__'
    0x16,0x4e, // STORE_NAME '__module__'
    0x10,0x12, // LOAD_CONST_STRING 'TopLevelCoro'
    0x16,0x4f, // STORE_NAME '__qualname__'
    0x11,0x54, // LOAD_NAME 'staticmethod'
    0x32,0x00, // MAKE_FUNCTION 0
    0x34,0x01, // CALL_FUNCTION 1
    0x16,0x2f, // STORE_NAME 'set'
    0x11,0x54, // LOAD_NAME 'staticmethod'
    0x32,0x01, // MAKE_FUNCTION 1
    0x34,0x01, // CALL_FUNCTION 1
    0x16,0x22, // STORE_NAME 'send'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
// child of asyncio_core_TopLevelCoro
// frozen bytecode for file asyncio/core.py, scope asyncio_core_TopLevelCoro_set
static const byte fun_data_asyncio_core_TopLevelCoro_set[17] = {
    0x1a,0x06, // prelude
    0x2f,0x30,0x31, // names: set, resolve, reject
     // code info
    0xb0, // LOAD_FAST 0
    0x12,0x12, // LOAD_GLOBAL 'TopLevelCoro'
    0x18,0x30, // STORE_ATTR 'resolve'
    0xb1, // LOAD_FAST 1
    0x12,0x12, // LOAD_GLOBAL 'TopLevelCoro'
    0x18,0x31, // STORE_ATTR 'reject'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_TopLevelCoro_set = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_TopLevelCoro_set,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 17,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 4,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 2,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 47,
        .line_info = fun_data_asyncio_core_TopLevelCoro_set + 5,
        .line_info_top = fun_data_asyncio_core_TopLevelCoro_set + 5,
        .opcodes = fun_data_asyncio_core_TopLevelCoro_set + 5,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_TopLevelCoro_set fun_data_asyncio_core_TopLevelCoro_set[0]
#endif

// child of asyncio_core_TopLevelCoro
// frozen bytecode for file asyncio/core.py, scope asyncio_core_TopLevelCoro_send
static const byte fun_data_asyncio_core_TopLevelCoro_send[13] = {
    0x11,0x04, // prelude
    0x22,0x5e, // names: send, value
     // code info
    0x12,0x12, // LOAD_GLOBAL 'TopLevelCoro'
    0x14,0x30, // LOAD_METHOD 'resolve'
    0x36,0x00, // CALL_METHOD 0
    0x59, // POP_TOP
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_TopLevelCoro_send = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_TopLevelCoro_send,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 13,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 3,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 34,
        .line_info = fun_data_asyncio_core_TopLevelCoro_send + 4,
        .line_info_top = fun_data_asyncio_core_TopLevelCoro_send + 4,
        .opcodes = fun_data_asyncio_core_TopLevelCoro_send + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_TopLevelCoro_send fun_data_asyncio_core_TopLevelCoro_send[0]
#endif

static const mp_raw_code_t *const children_asyncio_core_TopLevelCoro[] = {
    (const mp_raw_code_t *)&proto_fun_asyncio_core_TopLevelCoro_set,
    (const mp_raw_code_t *)&proto_fun_asyncio_core_TopLevelCoro_send,
};

static const mp_raw_code_truncated_t proto_fun_asyncio_core_TopLevelCoro = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_TopLevelCoro,
    .children = (void *)&children_asyncio_core_TopLevelCoro,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 29,
    .n_children = 2,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 2,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 0,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 18,
        .line_info = fun_data_asyncio_core_TopLevelCoro + 3,
        .line_info_top = fun_data_asyncio_core_TopLevelCoro + 3,
        .opcodes = fun_data_asyncio_core_TopLevelCoro + 3,
    },
    #endif
    #endif
};

// child of asyncio_core__lt_module_gt_
// frozen bytecode for file asyncio/core.py, scope asyncio_core_ThenableEvent
static const byte fun_data_asyncio_core_ThenableEvent[41] = {
    0x08,0x02, // prelude
    0x13, // names: ThenableEvent
     // code info
    0x11,0x4d, // LOAD_NAME '__name__'
    0x16,0x4e, // STORE_NAME '__module__'
    0x10,0x13, // LOAD_CONST_STRING 'ThenableEvent'
    0x16,0x4f, // STORE_NAME '__qualname__'
    0x32,0x00, // MAKE_FUNCTION 0
    0x16,0x2a, // STORE_NAME '__init__'
    0x51, // LOAD_CONST_NONE
    0x2a,0x01, // BUILD_TUPLE 1
    0x53, // LOAD_NULL
    0x33,0x01, // MAKE_FUNCTION_DEFARGS 1
    0x16,0x2f, // STORE_NAME 'set'
    0x51, // LOAD_CONST_NONE
    0x2a,0x01, // BUILD_TUPLE 1
    0x53, // LOAD_NULL
    0x33,0x02, // MAKE_FUNCTION_DEFARGS 2
    0x16,0x34, // STORE_NAME 'cancel'
    0x32,0x03, // MAKE_FUNCTION 3
    0x16,0x39, // STORE_NAME 'remove'
    0x32,0x04, // MAKE_FUNCTION 4
    0x16,0x3a, // STORE_NAME 'wait'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
// child of asyncio_core_ThenableEvent
// frozen bytecode for file asyncio/core.py, scope asyncio_core_ThenableEvent___init__
static const byte fun_data_asyncio_core_ThenableEvent___init__[23] = {
    0x2a,0x06, // prelude
    0x2a,0x5d,0x5f, // names: __init__, self, thenable
     // code info
    0x51, // LOAD_CONST_NONE
    0xb0, // LOAD_FAST 0
    0x18,0x32, // STORE_ATTR 'waiting'
    0xb1, // LOAD_FAST 1
    0x14,0x33, // LOAD_METHOD 'then'
    0xb0, // LOAD_FAST 0
    0x13,0x2f, // LOAD_ATTR 'set'
    0xb0, // LOAD_FAST 0
    0x13,0x34, // LOAD_ATTR 'cancel'
    0x36,0x02, // CALL_METHOD 2
    0x59, // POP_TOP
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_ThenableEvent___init__ = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_ThenableEvent___init__,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 23,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 6,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 2,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 42,
        .line_info = fun_data_asyncio_core_ThenableEvent___init__ + 5,
        .line_info_top = fun_data_asyncio_core_ThenableEvent___init__ + 5,
        .opcodes = fun_data_asyncio_core_ThenableEvent___init__ + 5,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_ThenableEvent___init__ fun_data_asyncio_core_ThenableEvent___init__[0]
#endif

// child of asyncio_core_ThenableEvent
// frozen bytecode for file asyncio/core.py, scope asyncio_core_ThenableEvent_set
static const byte fun_data_asyncio_core_ThenableEvent_set[31] = {
    0xa2,0x01,0x06, // prelude
    0x2f,0x5d,0x5e, // names: set, self, value
     // code info
    0xb1, // LOAD_FAST 1
    0xb0, // LOAD_FAST 0
    0x18,0x35, // STORE_ATTR 'result'
    0xb0, // LOAD_FAST 0
    0x13,0x32, // LOAD_ATTR 'waiting'
    0x44,0x4e, // POP_JUMP_IF_FALSE 14
    0x12,0x59, // LOAD_GLOBAL '_task_queue'
    0x14,0x24, // LOAD_METHOD 'push'
    0xb0, // LOAD_FAST 0
    0x13,0x32, // LOAD_ATTR 'waiting'
    0x36,0x01, // CALL_METHOD 1
    0x59, // POP_TOP
    0x51, // LOAD_CONST_NONE
    0xb0, // LOAD_FAST 0
    0x18,0x32, // STORE_ATTR 'waiting'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_ThenableEvent_set = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_ThenableEvent_set,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 31,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 5,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 2,
        .n_kwonly_args = 0,
        .n_def_pos_args = 1,
        .qstr_block_name_idx = 47,
        .line_info = fun_data_asyncio_core_ThenableEvent_set + 6,
        .line_info_top = fun_data_asyncio_core_ThenableEvent_set + 6,
        .opcodes = fun_data_asyncio_core_ThenableEvent_set + 6,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_ThenableEvent_set fun_data_asyncio_core_ThenableEvent_set[0]
#endif

// child of asyncio_core_ThenableEvent
// frozen bytecode for file asyncio/core.py, scope asyncio_core_ThenableEvent_cancel
static const byte fun_data_asyncio_core_ThenableEvent_cancel[53] = {
    0xca,0x01,0x06, // prelude
    0x34,0x5d,0x5e, // names: cancel, self, value
     // code info
    0x12,0x08, // LOAD_GLOBAL 'jsffi'
    0x14,0x36, // LOAD_METHOD 'JsException'
    0xb1, // LOAD_FAST 1
    0x12,0x60, // LOAD_GLOBAL 'getattr'
    0xb1, // LOAD_FAST 1
    0x10,0x37, // LOAD_CONST_STRING 'name'
    0x51, // LOAD_CONST_NONE
    0x34,0x03, // CALL_FUNCTION 3
    0x12,0x60, // LOAD_GLOBAL 'getattr'
    0xb1, // LOAD_FAST 1
    0x10,0x0e, // LOAD_CONST_STRING 'message'
    0x51, // LOAD_CONST_NONE
    0x34,0x03, // CALL_FUNCTION 3
    0x36,0x03, // CALL_METHOD 3
    0xb0, // LOAD_FAST 0
    0x18,0x38, // STORE_ATTR 'error'
    0xb0, // LOAD_FAST 0
    0x13,0x32, // LOAD_ATTR 'waiting'
    0x44,0x4e, // POP_JUMP_IF_FALSE 14
    0x12,0x59, // LOAD_GLOBAL '_task_queue'
    0x14,0x24, // LOAD_METHOD 'push'
    0xb0, // LOAD_FAST 0
    0x13,0x32, // LOAD_ATTR 'waiting'
    0x36,0x01, // CALL_METHOD 1
    0x59, // POP_TOP
    0x51, // LOAD_CONST_NONE
    0xb0, // LOAD_FAST 0
    0x18,0x32, // STORE_ATTR 'waiting'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_ThenableEvent_cancel = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_ThenableEvent_cancel,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 53,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 10,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 2,
        .n_kwonly_args = 0,
        .n_def_pos_args = 1,
        .qstr_block_name_idx = 52,
        .line_info = fun_data_asyncio_core_ThenableEvent_cancel + 6,
        .line_info_top = fun_data_asyncio_core_ThenableEvent_cancel + 6,
        .opcodes = fun_data_asyncio_core_ThenableEvent_cancel + 6,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_ThenableEvent_cancel fun_data_asyncio_core_ThenableEvent_cancel[0]
#endif

// child of asyncio_core_ThenableEvent
// frozen bytecode for file asyncio/core.py, scope asyncio_core_ThenableEvent_remove
static const byte fun_data_asyncio_core_ThenableEvent_remove[11] = {
    0x1a,0x06, // prelude
    0x39,0x5d,0x61, // names: remove, self, task
     // code info
    0x51, // LOAD_CONST_NONE
    0xb0, // LOAD_FAST 0
    0x18,0x32, // STORE_ATTR 'waiting'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_ThenableEvent_remove = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_ThenableEvent_remove,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 11,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 4,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 2,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 57,
        .line_info = fun_data_asyncio_core_ThenableEvent_remove + 5,
        .line_info_top = fun_data_asyncio_core_ThenableEvent_remove + 5,
        .opcodes = fun_data_asyncio_core_ThenableEvent_remove + 5,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_ThenableEvent_remove fun_data_asyncio_core_ThenableEvent_remove[0]
#endif

// child of asyncio_core_ThenableEvent
// frozen bytecode for file asyncio/core.py, scope asyncio_core_ThenableEvent_wait
static const byte fun_data_asyncio_core_ThenableEvent_wait[35] = {
    0x99,0x40,0x04, // prelude
    0x3a,0x5d, // names: wait, self
     // code info
    0x12,0x4c, // LOAD_GLOBAL 'cur_task'
    0xb0, // LOAD_FAST 0
    0x18,0x32, // STORE_ATTR 'waiting'
    0xb0, // LOAD_FAST 0
    0x12,0x4c, // LOAD_GLOBAL 'cur_task'
    0x18,0x20, // STORE_ATTR 'data'
    0x51, // LOAD_CONST_NONE
    0x67, // YIELD_VALUE
    0x59, // POP_TOP
    0x12,0x5b, // LOAD_GLOBAL 'hasattr'
    0xb0, // LOAD_FAST 0
    0x10,0x38, // LOAD_CONST_STRING 'error'
    0x34,0x02, // CALL_FUNCTION 2
    0x44,0x44, // POP_JUMP_IF_FALSE 4
    0xb0, // LOAD_FAST 0
    0x13,0x38, // LOAD_ATTR 'error'
    0x65, // RAISE_OBJ
    0xb0, // LOAD_FAST 0
    0x13,0x35, // LOAD_ATTR 'result'
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_ThenableEvent_wait = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 1,
    .fun_data = fun_data_asyncio_core_ThenableEvent_wait,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 35,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 4,
        .n_exc_stack = 0,
        .scope_flags = 1,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 58,
        .line_info = fun_data_asyncio_core_ThenableEvent_wait + 5,
        .line_info_top = fun_data_asyncio_core_ThenableEvent_wait + 5,
        .opcodes = fun_data_asyncio_core_ThenableEvent_wait + 5,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_ThenableEvent_wait fun_data_asyncio_core_ThenableEvent_wait[0]
#endif

static const mp_raw_code_t *const children_asyncio_core_ThenableEvent[] = {
    (const mp_raw_code_t *)&proto_fun_asyncio_core_ThenableEvent___init__,
    (const mp_raw_code_t *)&proto_fun_asyncio_core_ThenableEvent_set,
    (const mp_raw_code_t *)&proto_fun_asyncio_core_ThenableEvent_cancel,
    (const mp_raw_code_t *)&proto_fun_asyncio_core_ThenableEvent_remove,
    (const mp_raw_code_t *)&proto_fun_asyncio_core_ThenableEvent_wait,
};

static const mp_raw_code_truncated_t proto_fun_asyncio_core_ThenableEvent = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_ThenableEvent,
    .children = (void *)&children_asyncio_core_ThenableEvent,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 41,
    .n_children = 5,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 2,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 0,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 19,
        .line_info = fun_data_asyncio_core_ThenableEvent + 3,
        .line_info_top = fun_data_asyncio_core_ThenableEvent + 3,
        .opcodes = fun_data_asyncio_core_ThenableEvent + 3,
    },
    #endif
    #endif
};

// child of asyncio_core__lt_module_gt_
// frozen bytecode for file asyncio/core.py, scope asyncio_core__promote_to_task
static const byte fun_data_asyncio_core__promote_to_task[21] = {
    0x19,0x04, // prelude
    0x18,0x55, // names: _promote_to_task, aw
     // code info
    0x12,0x56, // LOAD_GLOBAL 'isinstance'
    0xb0, // LOAD_FAST 0
    0x12,0x0a, // LOAD_GLOBAL 'Task'
    0x34,0x02, // CALL_FUNCTION 2
    0x44,0x42, // POP_JUMP_IF_FALSE 2
    0xb0, // LOAD_FAST 0
    0x63, // RETURN_VALUE
    0x12,0x26, // LOAD_GLOBAL 'create_task'
    0xb0, // LOAD_FAST 0
    0x34,0x01, // CALL_FUNCTION 1
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core__promote_to_task = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core__promote_to_task,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 21,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 4,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 24,
        .line_info = fun_data_asyncio_core__promote_to_task + 4,
        .line_info_top = fun_data_asyncio_core__promote_to_task + 4,
        .opcodes = fun_data_asyncio_core__promote_to_task + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core__promote_to_task fun_data_asyncio_core__promote_to_task[0]
#endif

// child of asyncio_core__lt_module_gt_
// frozen bytecode for file asyncio/core.py, scope asyncio_core__schedule_run_iter
static const byte fun_data_asyncio_core__schedule_run_iter[33] = {
    0x21,0x04, // prelude
    0x19,0x57, // names: _schedule_run_iter, dt
     // code info
    0x12,0x49, // LOAD_GLOBAL 'asyncio_timer'
    0x51, // LOAD_CONST_NONE
    0xde, // BINARY_OP 7 <is>
    0xd3, // UNARY_OP 3 <not>
    0x44,0x49, // POP_JUMP_IF_FALSE 9
    0x12,0x07, // LOAD_GLOBAL 'js'
    0x14,0x1a, // LOAD_METHOD 'clearTimeout'
    0x12,0x49, // LOAD_GLOBAL 'asyncio_timer'
    0x36,0x01, // CALL_METHOD 1
    0x59, // POP_TOP
    0x12,0x07, // LOAD_GLOBAL 'js'
    0x14,0x1b, // LOAD_METHOD 'setTimeout'
    0x12,0x1c, // LOAD_GLOBAL '_run_iter'
    0xb0, // LOAD_FAST 0
    0x36,0x02, // CALL_METHOD 2
    0x17,0x49, // STORE_GLOBAL 'asyncio_timer'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core__schedule_run_iter = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core__schedule_run_iter,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 33,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 5,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 25,
        .line_info = fun_data_asyncio_core__schedule_run_iter + 4,
        .line_info_top = fun_data_asyncio_core__schedule_run_iter + 4,
        .opcodes = fun_data_asyncio_core__schedule_run_iter + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core__schedule_run_iter fun_data_asyncio_core__schedule_run_iter[0]
#endif

// child of asyncio_core__lt_module_gt_
// frozen bytecode for file asyncio/core.py, scope asyncio_core__run_iter
static const byte fun_data_asyncio_core__run_iter[276] = {
    0xe8,0x02,0x02, // prelude
    0x1c, // names: _run_iter
     // code info
    0x12,0x0c, // LOAD_GLOBAL 'CancelledError'
    0x12,0x47, // LOAD_GLOBAL 'Exception'
    0x2a,0x02, // BUILD_TUPLE 2
    0xc0, // STORE_FAST 0
    0x12,0x0c, // LOAD_GLOBAL 'CancelledError'
    0x12,0x58, // LOAD_GLOBAL 'StopIteration'
    0x2a,0x02, // BUILD_TUPLE 2
    0xc1, // STORE_FAST 1
    0x12,0x59, // LOAD_GLOBAL '_task_queue'
    0x14,0x1d, // LOAD_METHOD 'peek'
    0x36,0x00, // CALL_METHOD 0
    0xc2, // STORE_FAST 2
    0xb2, // LOAD_FAST 2
    0x44,0x53, // POP_JUMP_IF_FALSE 19
    0x12,0x52, // LOAD_GLOBAL 'max'
    0x80, // LOAD_CONST_SMALL_INT 0
    0x12,0x03, // LOAD_GLOBAL 'ticks_diff'
    0xb2, // LOAD_FAST 2
    0x13,0x1e, // LOAD_ATTR 'ph_key'
    0x12,0x45, // LOAD_GLOBAL 'ticks'
    0x34,0x00, // CALL_FUNCTION 0
    0x34,0x02, // CALL_FUNCTION 2
    0x34,0x02, // CALL_FUNCTION 2
    0xc3, // STORE_FAST 3
    0x42,0x46, // JUMP 6
    0x12,0x4b, // LOAD_GLOBAL '_top_level_task'
    0x17,0x4c, // STORE_GLOBAL 'cur_task'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
    0xb3, // LOAD_FAST 3
    0x80, // LOAD_CONST_SMALL_INT 0
    0xd8, // BINARY_OP 1 __gt__
    0x44,0x4c, // POP_JUMP_IF_FALSE 12
    0x12,0x4b, // LOAD_GLOBAL '_top_level_task'
    0x17,0x4c, // STORE_GLOBAL 'cur_task'
    0x12,0x19, // LOAD_GLOBAL '_schedule_run_iter'
    0xb3, // LOAD_FAST 3
    0x34,0x01, // CALL_FUNCTION 1
    0x59, // POP_TOP
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
    0x12,0x59, // LOAD_GLOBAL '_task_queue'
    0x14,0x1f, // LOAD_METHOD 'pop'
    0x36,0x00, // CALL_METHOD 0
    0xc2, // STORE_FAST 2
    0xb2, // LOAD_FAST 2
    0x17,0x4c, // STORE_GLOBAL 'cur_task'
    0x48,0x22, // SETUP_EXCEPT 34
    0xb2, // LOAD_FAST 2
    0x13,0x20, // LOAD_ATTR 'data'
    0xc4, // STORE_FAST 4
    0xb4, // LOAD_FAST 4
    0x43,0x4b, // POP_JUMP_IF_TRUE 11
    0xb2, // LOAD_FAST 2
    0x13,0x21, // LOAD_ATTR 'coro'
    0x14,0x22, // LOAD_METHOD 'send'
    0x51, // LOAD_CONST_NONE
    0x36,0x01, // CALL_METHOD 1
    0x59, // POP_TOP
    0x42,0x4d, // JUMP 13
    0x51, // LOAD_CONST_NONE
    0xb2, // LOAD_FAST 2
    0x18,0x20, // STORE_ATTR 'data'
    0xb2, // LOAD_FAST 2
    0x13,0x21, // LOAD_ATTR 'coro'
    0x14,0x23, // LOAD_METHOD 'throw'
    0xb4, // LOAD_FAST 4
    0x36,0x01, // CALL_METHOD 1
    0x59, // POP_TOP
    0x4a,0x9b,0x01, // POP_EXCEPT_JUMP 155
    0x57, // DUP_TOP
    0xb0, // LOAD_FAST 0
    0xdf, // BINARY_OP 8 <exception match>
    0x44,0x94,0x81, // POP_JUMP_IF_FALSE 148
    0xc5, // STORE_FAST 5
    0x49,0x89,0x01, // SETUP_FINALLY 137
    0xb2, // LOAD_FAST 2
    0x13,0x16, // LOAD_ATTR 'state'
    0x44,0xe0,0x80, // POP_JUMP_IF_FALSE 96
    0x50, // LOAD_CONST_FALSE
    0xc6, // STORE_FAST 6
    0xb2, // LOAD_FAST 2
    0x13,0x16, // LOAD_ATTR 'state'
    0x52, // LOAD_CONST_TRUE
    0xde, // BINARY_OP 7 <is>
    0x44,0x46, // POP_JUMP_IF_FALSE 6
    0x51, // LOAD_CONST_NONE
    0xb2, // LOAD_FAST 2
    0x18,0x16, // STORE_ATTR 'state'
    0x42,0x78, // JUMP 56
    0x12,0x5a, // LOAD_GLOBAL 'callable'
    0xb2, // LOAD_FAST 2
    0x13,0x16, // LOAD_ATTR 'state'
    0x34,0x01, // CALL_FUNCTION 1
    0x44,0x50, // POP_JUMP_IF_FALSE 16
    0xb2, // LOAD_FAST 2
    0x14,0x16, // LOAD_METHOD 'state'
    0xb2, // LOAD_FAST 2
    0xb5, // LOAD_FAST 5
    0x36,0x02, // CALL_METHOD 2
    0x59, // POP_TOP
    0x50, // LOAD_CONST_FALSE
    0xb2, // LOAD_FAST 2
    0x18,0x16, // STORE_ATTR 'state'
    0x52, // LOAD_CONST_TRUE
    0xc6, // STORE_FAST 6
    0x42,0x5f, // JUMP 31
    0x42,0x50, // JUMP 16
    0x12,0x59, // LOAD_GLOBAL '_task_queue'
    0x14,0x24, // LOAD_METHOD 'push'
    0xb2, // LOAD_FAST 2
    0x13,0x16, // LOAD_ATTR 'state'
    0x14,0x1f, // LOAD_METHOD 'pop'
    0x36,0x00, // CALL_METHOD 0
    0x36,0x01, // CALL_METHOD 1
    0x59, // POP_TOP
    0x52, // LOAD_CONST_TRUE
    0xc6, // STORE_FAST 6
    0xb2, // LOAD_FAST 2
    0x13,0x16, // LOAD_ATTR 'state'
    0x14,0x1d, // LOAD_METHOD 'peek'
    0x36,0x00, // CALL_METHOD 0
    0x43,0x27, // POP_JUMP_IF_TRUE -25
    0x50, // LOAD_CONST_FALSE
    0xb2, // LOAD_FAST 2
    0x18,0x16, // STORE_ATTR 'state'
    0xb6, // LOAD_FAST 6
    0x43,0x50, // POP_JUMP_IF_TRUE 16
    0x12,0x56, // LOAD_GLOBAL 'isinstance'
    0xb5, // LOAD_FAST 5
    0xb1, // LOAD_FAST 1
    0x34,0x02, // CALL_FUNCTION 2
    0x43,0x48, // POP_JUMP_IF_TRUE 8
    0x12,0x59, // LOAD_GLOBAL '_task_queue'
    0x14,0x24, // LOAD_METHOD 'push'
    0xb2, // LOAD_FAST 2
    0x36,0x01, // CALL_METHOD 1
    0x59, // POP_TOP
    0xb5, // LOAD_FAST 5
    0xb2, // LOAD_FAST 2
    0x18,0x20, // STORE_ATTR 'data'
    0x42,0x62, // JUMP 34
    0xb2, // LOAD_FAST 2
    0x13,0x16, // LOAD_ATTR 'state'
    0x51, // LOAD_CONST_NONE
    0xde, // BINARY_OP 7 <is>
    0x44,0x5b, // POP_JUMP_IF_FALSE 27
    0xb4, // LOAD_FAST 4
    0xb2, // LOAD_FAST 2
    0x18,0x20, // STORE_ATTR 'data'
    0xb4, // LOAD_FAST 4
    0x12,0x48, // LOAD_GLOBAL '_exc_context'
    0x10,0x0f, // LOAD_CONST_STRING 'exception'
    0x56, // STORE_SUBSCR
    0xb2, // LOAD_FAST 2
    0x12,0x48, // LOAD_GLOBAL '_exc_context'
    0x10,0x10, // LOAD_CONST_STRING 'future'
    0x56, // STORE_SUBSCR
    0x12,0x14, // LOAD_GLOBAL 'Loop'
    0x14,0x25, // LOAD_METHOD 'call_exception_handler'
    0x12,0x48, // LOAD_GLOBAL '_exc_context'
    0x36,0x01, // CALL_METHOD 1
    0x59, // POP_TOP
    0x42,0x40, // JUMP 0
    0x51, // LOAD_CONST_NONE
    0x51, // LOAD_CONST_NONE
    0xc5, // STORE_FAST 5
    0x28,0x05, // DELETE_FAST 5
    0x5d, // END_FINALLY
    0x4a,0x01, // POP_EXCEPT_JUMP 1
    0x5d, // END_FINALLY
    0x42,0x80,0x7e, // JUMP -256
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core__run_iter = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core__run_iter,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 276,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 14,
        .n_exc_stack = 2,
        .scope_flags = 0,
        .n_pos_args = 0,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 28,
        .line_info = fun_data_asyncio_core__run_iter + 4,
        .line_info_top = fun_data_asyncio_core__run_iter + 4,
        .opcodes = fun_data_asyncio_core__run_iter + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core__run_iter fun_data_asyncio_core__run_iter[0]
#endif

// child of asyncio_core__lt_module_gt_
// frozen bytecode for file asyncio/core.py, scope asyncio_core_create_task
static const byte fun_data_asyncio_core_create_task[40] = {
    0x21,0x04, // prelude
    0x26,0x21, // names: create_task, coro
     // code info
    0x12,0x5b, // LOAD_GLOBAL 'hasattr'
    0xb0, // LOAD_FAST 0
    0x10,0x22, // LOAD_CONST_STRING 'send'
    0x34,0x02, // CALL_FUNCTION 2
    0x43,0x47, // POP_JUMP_IF_TRUE 7
    0x12,0x5c, // LOAD_GLOBAL 'TypeError'
    0x23,0x01, // LOAD_CONST_OBJ 1
    0x34,0x01, // CALL_FUNCTION 1
    0x65, // RAISE_OBJ
    0x12,0x0a, // LOAD_GLOBAL 'Task'
    0xb0, // LOAD_FAST 0
    0x12,0x4a, // LOAD_GLOBAL 'globals'
    0x34,0x00, // CALL_FUNCTION 0
    0x34,0x02, // CALL_FUNCTION 2
    0xc1, // STORE_FAST 1
    0x12,0x59, // LOAD_GLOBAL '_task_queue'
    0x14,0x24, // LOAD_METHOD 'push'
    0xb1, // LOAD_FAST 1
    0x36,0x01, // CALL_METHOD 1
    0x59, // POP_TOP
    0xb1, // LOAD_FAST 1
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_create_task = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_create_task,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 40,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 5,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 38,
        .line_info = fun_data_asyncio_core_create_task + 4,
        .line_info_top = fun_data_asyncio_core_create_task + 4,
        .opcodes = fun_data_asyncio_core_create_task + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_create_task fun_data_asyncio_core_create_task[0]
#endif

// child of asyncio_core__lt_module_gt_
// frozen bytecode for file asyncio/core.py, scope asyncio_core_Loop
static const byte fun_data_asyncio_core_Loop[40] = {
    0x00,0x02, // prelude
    0x14, // names: Loop
     // code info
    0x11,0x4d, // LOAD_NAME '__name__'
    0x16,0x4e, // STORE_NAME '__module__'
    0x10,0x14, // LOAD_CONST_STRING 'Loop'
    0x16,0x4f, // STORE_NAME '__qualname__'
    0x51, // LOAD_CONST_NONE
    0x16,0x3d, // STORE_NAME '_exc_handler'
    0x32,0x00, // MAKE_FUNCTION 0
    0x16,0x26, // STORE_NAME 'create_task'
    0x32,0x01, // MAKE_FUNCTION 1
    0x16,0x3b, // STORE_NAME 'close'
    0x32,0x02, // MAKE_FUNCTION 2
    0x16,0x3c, // STORE_NAME 'set_exception_handler'
    0x32,0x03, // MAKE_FUNCTION 3
    0x16,0x3e, // STORE_NAME 'get_exception_handler'
    0x32,0x04, // MAKE_FUNCTION 4
    0x16,0x3f, // STORE_NAME 'default_exception_handler'
    0x32,0x05, // MAKE_FUNCTION 5
    0x16,0x25, // STORE_NAME 'call_exception_handler'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
// child of asyncio_core_Loop
// frozen bytecode for file asyncio/core.py, scope asyncio_core_Loop_create_task
static const byte fun_data_asyncio_core_Loop_create_task[10] = {
    0x11,0x04, // prelude
    0x26,0x21, // names: create_task, coro
     // code info
    0x12,0x26, // LOAD_GLOBAL 'create_task'
    0xb0, // LOAD_FAST 0
    0x34,0x01, // CALL_FUNCTION 1
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_Loop_create_task = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_Loop_create_task,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 10,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 3,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 38,
        .line_info = fun_data_asyncio_core_Loop_create_task + 4,
        .line_info_top = fun_data_asyncio_core_Loop_create_task + 4,
        .opcodes = fun_data_asyncio_core_Loop_create_task + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_Loop_create_task fun_data_asyncio_core_Loop_create_task[0]
#endif

// child of asyncio_core_Loop
// frozen bytecode for file asyncio/core.py, scope asyncio_core_Loop_close
static const byte fun_data_asyncio_core_Loop_close[5] = {
    0x00,0x02, // prelude
    0x3b, // names: close
     // code info
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_Loop_close = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_Loop_close,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 5,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 1,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 0,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 59,
        .line_info = fun_data_asyncio_core_Loop_close + 3,
        .line_info_top = fun_data_asyncio_core_Loop_close + 3,
        .opcodes = fun_data_asyncio_core_Loop_close + 3,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_Loop_close fun_data_asyncio_core_Loop_close[0]
#endif

// child of asyncio_core_Loop
// frozen bytecode for file asyncio/core.py, scope asyncio_core_Loop_set_exception_handler
static const byte fun_data_asyncio_core_Loop_set_exception_handler[11] = {
    0x11,0x04, // prelude
    0x3c,0x62, // names: set_exception_handler, handler
     // code info
    0xb0, // LOAD_FAST 0
    0x12,0x14, // LOAD_GLOBAL 'Loop'
    0x18,0x3d, // STORE_ATTR '_exc_handler'
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_Loop_set_exception_handler = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_Loop_set_exception_handler,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 11,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 3,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 60,
        .line_info = fun_data_asyncio_core_Loop_set_exception_handler + 4,
        .line_info_top = fun_data_asyncio_core_Loop_set_exception_handler + 4,
        .opcodes = fun_data_asyncio_core_Loop_set_exception_handler + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_Loop_set_exception_handler fun_data_asyncio_core_Loop_set_exception_handler[0]
#endif

// child of asyncio_core_Loop
// frozen bytecode for file asyncio/core.py, scope asyncio_core_Loop_get_exception_handler
static const byte fun_data_asyncio_core_Loop_get_exception_handler[8] = {
    0x00,0x02, // prelude
    0x3e, // names: get_exception_handler
     // code info
    0x12,0x14, // LOAD_GLOBAL 'Loop'
    0x13,0x3d, // LOAD_ATTR '_exc_handler'
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_Loop_get_exception_handler = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_Loop_get_exception_handler,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 8,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 1,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 0,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 62,
        .line_info = fun_data_asyncio_core_Loop_get_exception_handler + 3,
        .line_info_top = fun_data_asyncio_core_Loop_get_exception_handler + 3,
        .opcodes = fun_data_asyncio_core_Loop_get_exception_handler + 3,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_Loop_get_exception_handler fun_data_asyncio_core_Loop_get_exception_handler[0]
#endif

// child of asyncio_core_Loop
// frozen bytecode for file asyncio/core.py, scope asyncio_core_Loop_default_exception_handler
static const byte fun_data_asyncio_core_Loop_default_exception_handler[64] = {
    0x42,0x06, // prelude
    0x3f,0x63,0x64, // names: default_exception_handler, loop, context
     // code info
    0x12,0x65, // LOAD_GLOBAL 'print'
    0xb1, // LOAD_FAST 1
    0x10,0x0e, // LOAD_CONST_STRING 'message'
    0x55, // LOAD_SUBSCR
    0x10,0x40, // LOAD_CONST_STRING 'file'
    0x12,0x06, // LOAD_GLOBAL 'sys'
    0x13,0x41, // LOAD_ATTR 'stderr'
    0x34,0x82,0x01, // CALL_FUNCTION 257
    0x59, // POP_TOP
    0x12,0x65, // LOAD_GLOBAL 'print'
    0x10,0x42, // LOAD_CONST_STRING 'future:'
    0xb1, // LOAD_FAST 1
    0x10,0x10, // LOAD_CONST_STRING 'future'
    0x55, // LOAD_SUBSCR
    0x10,0x43, // LOAD_CONST_STRING 'coro='
    0xb1, // LOAD_FAST 1
    0x10,0x10, // LOAD_CONST_STRING 'future'
    0x55, // LOAD_SUBSCR
    0x13,0x21, // LOAD_ATTR 'coro'
    0x10,0x40, // LOAD_CONST_STRING 'file'
    0x12,0x06, // LOAD_GLOBAL 'sys'
    0x13,0x41, // LOAD_ATTR 'stderr'
    0x34,0x82,0x04, // CALL_FUNCTION 260
    0x59, // POP_TOP
    0x12,0x06, // LOAD_GLOBAL 'sys'
    0x14,0x44, // LOAD_METHOD 'print_exception'
    0xb1, // LOAD_FAST 1
    0x10,0x0f, // LOAD_CONST_STRING 'exception'
    0x55, // LOAD_SUBSCR
    0x12,0x06, // LOAD_GLOBAL 'sys'
    0x13,0x41, // LOAD_ATTR 'stderr'
    0x36,0x02, // CALL_METHOD 2
    0x59, // POP_TOP
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_Loop_default_exception_handler = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_Loop_default_exception_handler,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 64,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 9,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 2,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 63,
        .line_info = fun_data_asyncio_core_Loop_default_exception_handler + 5,
        .line_info_top = fun_data_asyncio_core_Loop_default_exception_handler + 5,
        .opcodes = fun_data_asyncio_core_Loop_default_exception_handler + 5,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_Loop_default_exception_handler fun_data_asyncio_core_Loop_default_exception_handler[0]
#endif

// child of asyncio_core_Loop
// frozen bytecode for file asyncio/core.py, scope asyncio_core_Loop_call_exception_handler
static const byte fun_data_asyncio_core_Loop_call_exception_handler[22] = {
    0x19,0x04, // prelude
    0x25,0x64, // names: call_exception_handler, context
     // code info
    0x12,0x14, // LOAD_GLOBAL 'Loop'
    0x13,0x3d, // LOAD_ATTR '_exc_handler'
    0x45,0x04, // JUMP_IF_TRUE_OR_POP 4
    0x12,0x14, // LOAD_GLOBAL 'Loop'
    0x13,0x3f, // LOAD_ATTR 'default_exception_handler'
    0x12,0x14, // LOAD_GLOBAL 'Loop'
    0xb0, // LOAD_FAST 0
    0x34,0x02, // CALL_FUNCTION 2
    0x59, // POP_TOP
    0x51, // LOAD_CONST_NONE
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_Loop_call_exception_handler = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_Loop_call_exception_handler,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 22,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 4,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 1,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 37,
        .line_info = fun_data_asyncio_core_Loop_call_exception_handler + 4,
        .line_info_top = fun_data_asyncio_core_Loop_call_exception_handler + 4,
        .opcodes = fun_data_asyncio_core_Loop_call_exception_handler + 4,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_Loop_call_exception_handler fun_data_asyncio_core_Loop_call_exception_handler[0]
#endif

static const mp_raw_code_t *const children_asyncio_core_Loop[] = {
    (const mp_raw_code_t *)&proto_fun_asyncio_core_Loop_create_task,
    (const mp_raw_code_t *)&proto_fun_asyncio_core_Loop_close,
    (const mp_raw_code_t *)&proto_fun_asyncio_core_Loop_set_exception_handler,
    (const mp_raw_code_t *)&proto_fun_asyncio_core_Loop_get_exception_handler,
    (const mp_raw_code_t *)&proto_fun_asyncio_core_Loop_default_exception_handler,
    (const mp_raw_code_t *)&proto_fun_asyncio_core_Loop_call_exception_handler,
};

static const mp_raw_code_truncated_t proto_fun_asyncio_core_Loop = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_Loop,
    .children = (void *)&children_asyncio_core_Loop,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 40,
    .n_children = 6,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 1,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 0,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 20,
        .line_info = fun_data_asyncio_core_Loop + 3,
        .line_info_top = fun_data_asyncio_core_Loop + 3,
        .opcodes = fun_data_asyncio_core_Loop + 3,
    },
    #endif
    #endif
};

// child of asyncio_core__lt_module_gt_
// frozen bytecode for file asyncio/core.py, scope asyncio_core_get_event_loop
static const byte fun_data_asyncio_core_get_event_loop[6] = {
    0x00,0x02, // prelude
    0x27, // names: get_event_loop
     // code info
    0x12,0x14, // LOAD_GLOBAL 'Loop'
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_get_event_loop = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_get_event_loop,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 6,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 1,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 0,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 39,
        .line_info = fun_data_asyncio_core_get_event_loop + 3,
        .line_info_top = fun_data_asyncio_core_get_event_loop + 3,
        .opcodes = fun_data_asyncio_core_get_event_loop + 3,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_get_event_loop fun_data_asyncio_core_get_event_loop[0]
#endif

// child of asyncio_core__lt_module_gt_
// frozen bytecode for file asyncio/core.py, scope asyncio_core_current_task
static const byte fun_data_asyncio_core_current_task[6] = {
    0x00,0x02, // prelude
    0x28, // names: current_task
     // code info
    0x12,0x4c, // LOAD_GLOBAL 'cur_task'
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_current_task = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_current_task,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 6,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 1,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 0,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 40,
        .line_info = fun_data_asyncio_core_current_task + 3,
        .line_info_top = fun_data_asyncio_core_current_task + 3,
        .opcodes = fun_data_asyncio_core_current_task + 3,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_current_task fun_data_asyncio_core_current_task[0]
#endif

// child of asyncio_core__lt_module_gt_
// frozen bytecode for file asyncio/core.py, scope asyncio_core_new_event_loop
static const byte fun_data_asyncio_core_new_event_loop[14] = {
    0x08,0x02, // prelude
    0x29, // names: new_event_loop
     // code info
    0x12,0x09, // LOAD_GLOBAL 'TaskQueue'
    0x12,0x19, // LOAD_GLOBAL '_schedule_run_iter'
    0x34,0x01, // CALL_FUNCTION 1
    0x17,0x59, // STORE_GLOBAL '_task_queue'
    0x12,0x14, // LOAD_GLOBAL 'Loop'
    0x63, // RETURN_VALUE
};
#if MICROPY_PERSISTENT_CODE_SAVE
static const mp_raw_code_truncated_t proto_fun_asyncio_core_new_event_loop = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core_new_event_loop,
    .children = NULL,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 14,
    .n_children = 0,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 2,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 0,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 41,
        .line_info = fun_data_asyncio_core_new_event_loop + 3,
        .line_info_top = fun_data_asyncio_core_new_event_loop + 3,
        .opcodes = fun_data_asyncio_core_new_event_loop + 3,
    },
    #endif
    #endif
};
#else
#define proto_fun_asyncio_core_new_event_loop fun_data_asyncio_core_new_event_loop[0]
#endif

static const mp_raw_code_t *const children_asyncio_core__lt_module_gt_[] = {
    (const mp_raw_code_t *)&proto_fun_asyncio_core_CancelledError,
    (const mp_raw_code_t *)&proto_fun_asyncio_core_TimeoutError,
    (const mp_raw_code_t *)&proto_fun_asyncio_core_SingletonGenerator,
    (const mp_raw_code_t *)&proto_fun_asyncio_core_sleep_ms,
    (const mp_raw_code_t *)&proto_fun_asyncio_core_sleep,
    (const mp_raw_code_t *)&proto_fun_asyncio_core_TopLevelCoro,
    (const mp_raw_code_t *)&proto_fun_asyncio_core_ThenableEvent,
    (const mp_raw_code_t *)&proto_fun_asyncio_core__promote_to_task,
    (const mp_raw_code_t *)&proto_fun_asyncio_core__schedule_run_iter,
    (const mp_raw_code_t *)&proto_fun_asyncio_core__run_iter,
    (const mp_raw_code_t *)&proto_fun_asyncio_core_create_task,
    (const mp_raw_code_t *)&proto_fun_asyncio_core_Loop,
    (const mp_raw_code_t *)&proto_fun_asyncio_core_get_event_loop,
    (const mp_raw_code_t *)&proto_fun_asyncio_core_current_task,
    (const mp_raw_code_t *)&proto_fun_asyncio_core_new_event_loop,
};

static const mp_raw_code_truncated_t proto_fun_asyncio_core__lt_module_gt_ = {
    .proto_fun_indicator[0] = MP_PROTO_FUN_INDICATOR_RAW_CODE_0,
    .proto_fun_indicator[1] = MP_PROTO_FUN_INDICATOR_RAW_CODE_1,
    .kind = MP_CODE_BYTECODE,
    .is_generator = 0,
    .fun_data = fun_data_asyncio_core__lt_module_gt_,
    .children = (void *)&children_asyncio_core__lt_module_gt_,
    #if MICROPY_PERSISTENT_CODE_SAVE
    .fun_data_len = 207,
    .n_children = 15,
    #if MICROPY_EMIT_MACHINE_CODE
    .prelude_offset = 0,
    #endif
    #if MICROPY_PY_SYS_SETTRACE
    .line_of_definition = 0,
    .prelude = {
        .n_state = 4,
        .n_exc_stack = 0,
        .scope_flags = 0,
        .n_pos_args = 0,
        .n_kwonly_args = 0,
        .n_def_pos_args = 0,
        .qstr_block_name_idx = 1,
        .line_info = fun_data_asyncio_core__lt_module_gt_ + 3,
        .line_info_top = fun_data_asyncio_core__lt_module_gt_ + 3,
        .opcodes = fun_data_asyncio_core__lt_module_gt_ + 3,
    },
    #endif
    #endif
};

static const qstr_short_t const_qstr_table_data_asyncio_core[102] = {
    MP_QSTR_asyncio_slash_core_dot_py,
    MP_QSTR__lt_module_gt_,
    MP_QSTR_ticks_ms,
    MP_QSTR_ticks_diff,
    MP_QSTR_ticks_add,
    MP_QSTR_time,
    MP_QSTR_sys,
    MP_QSTR_js,
    MP_QSTR_jsffi,
    MP_QSTR_TaskQueue,
    MP_QSTR_Task,
    MP_QSTR__asyncio,
    MP_QSTR_CancelledError,
    MP_QSTR_TimeoutError,
    MP_QSTR_message,
    MP_QSTR_exception,
    MP_QSTR_future,
    MP_QSTR_SingletonGenerator,
    MP_QSTR_TopLevelCoro,
    MP_QSTR_ThenableEvent,
    MP_QSTR_Loop,
    MP_QSTR_sleep_ms,
    MP_QSTR_state,
    MP_QSTR_sleep,
    MP_QSTR__promote_to_task,
    MP_QSTR__schedule_run_iter,
    MP_QSTR_clearTimeout,
    MP_QSTR_setTimeout,
    MP_QSTR__run_iter,
    MP_QSTR_peek,
    MP_QSTR_ph_key,
    MP_QSTR_pop,
    MP_QSTR_data,
    MP_QSTR_coro,
    MP_QSTR_send,
    MP_QSTR_throw,
    MP_QSTR_push,
    MP_QSTR_call_exception_handler,
    MP_QSTR_create_task,
    MP_QSTR_get_event_loop,
    MP_QSTR_current_task,
    MP_QSTR_new_event_loop,
    MP_QSTR___init__,
    MP_QSTR_exc,
    MP_QSTR___iter__,
    MP_QSTR___next__,
    MP_QSTR___traceback__,
    MP_QSTR_set,
    MP_QSTR_resolve,
    MP_QSTR_reject,
    MP_QSTR_waiting,
    MP_QSTR_then,
    MP_QSTR_cancel,
    MP_QSTR_result,
    MP_QSTR_JsException,
    MP_QSTR_name,
    MP_QSTR_error,
    MP_QSTR_remove,
    MP_QSTR_wait,
    MP_QSTR_close,
    MP_QSTR_set_exception_handler,
    MP_QSTR__exc_handler,
    MP_QSTR_get_exception_handler,
    MP_QSTR_default_exception_handler,
    MP_QSTR_file,
    MP_QSTR_stderr,
    MP_QSTR_future_colon_,
    MP_QSTR_coro_equals_,
    MP_QSTR_print_exception,
    MP_QSTR_ticks,
    MP_QSTR_BaseException,
    MP_QSTR_Exception,
    MP_QSTR__exc_context,
    MP_QSTR_asyncio_timer,
    MP_QSTR_globals,
    MP_QSTR__top_level_task,
    MP_QSTR_cur_task,
    MP_QSTR___name__,
    MP_QSTR___module__,
    MP_QSTR___qualname__,
    MP_QSTR_t,
    MP_QSTR_sgen,
    MP_QSTR_max,
    MP_QSTR_int,
    MP_QSTR_staticmethod,
    MP_QSTR_aw,
    MP_QSTR_isinstance,
    MP_QSTR_dt,
    MP_QSTR_StopIteration,
    MP_QSTR__task_queue,
    MP_QSTR_callable,
    MP_QSTR_hasattr,
    MP_QSTR_TypeError,
    MP_QSTR_self,
    MP_QSTR_value,
    MP_QSTR_thenable,
    MP_QSTR_getattr,
    MP_QSTR_task,
    MP_QSTR_handler,
    MP_QSTR_loop,
    MP_QSTR_context,
    MP_QSTR_print,
};

// constants
static const mp_obj_str_t const_obj_asyncio_core_0 = {{&mp_type_str}, 64973, 31, (const byte*)"\x54\x61\x73\x6b\x20\x65\x78\x63\x65\x70\x74\x69\x6f\x6e\x20\x77\x61\x73\x6e\x27\x74\x20\x72\x65\x74\x72\x69\x65\x76\x65\x64"};

// constant table
static const mp_rom_obj_t const_obj_table_data_asyncio_core[2] = {
    MP_ROM_PTR(&const_obj_asyncio_core_0),
    MP_ROM_QSTR(MP_QSTR_coroutine_space_expected),
};

static const mp_frozen_module_t frozen_module_asyncio_core = {
    .constants = {
        .qstr_table = (qstr_short_t *)&const_qstr_table_data_asyncio_core,
        .obj_table = (mp_obj_t *)&const_obj_table_data_asyncio_core,
    },
    .proto_fun = &proto_fun_asyncio_core__lt_module_gt_,
};

////////////////////////////////////////////////////////////////////////////////
// collection of all frozen modules

const char mp_frozen_names[] = {
    #ifdef MP_FROZEN_STR_NAMES
    MP_FROZEN_STR_NAMES
    #endif
    "asyncio/event.py\0"
    "asyncio/funcs.py\0"
    "asyncio/lock.py\0"
    "asyncio/__init__.py\0"
    "asyncio/core.py\0"
    "\0"
};

const mp_frozen_module_t *const mp_frozen_mpy_content[] = {
    &frozen_module_asyncio_event,
    &frozen_module_asyncio_funcs,
    &frozen_module_asyncio_lock,
    &frozen_module_asyncio___init__,
    &frozen_module_asyncio_core,
};

#ifdef MICROPY_FROZEN_LIST_ITEM
MICROPY_FROZEN_LIST_ITEM("asyncio/event", "asyncio/event.py")
MICROPY_FROZEN_LIST_ITEM("asyncio/funcs", "asyncio/funcs.py")
MICROPY_FROZEN_LIST_ITEM("asyncio/lock", "asyncio/lock.py")
MICROPY_FROZEN_LIST_ITEM("asyncio", "asyncio/__init__.py")
MICROPY_FROZEN_LIST_ITEM("asyncio/core", "asyncio/core.py")
#endif

/*
byte sizes:
qstr content: 75 unique, 999 bytes
bc content: 2468
const str content: 31
const int content: 0
const obj content: 16
const table qstr content: 0 entries, 0 bytes
const table ptr content: 5 entries, 20 bytes
raw code content: 63 * 4 = 1008
mp_frozen_mpy_names_content: 87
mp_frozen_mpy_content_size: 20
total: 4649
*/
