
#include "nuitka/prelude.h"
#include "structseq.h"

// Sentinel PyObject to be used for all our call iterator endings. It will
// become a PyCObject pointing to NULL. It's address is unique, and that's
// enough for us to use it as sentinel value.
PyObject *_sentinel_value = NULL;

PyObject *Nuitka_dunder_compiled_value = NULL;

PyObject *const_int_0;
PyObject *const_str_dot;
PyObject *const_float_0_0;
PyObject *const_int_pos_1;
PyObject *const_str_empty;
PyObject *const_dict_empty;
PyObject *const_bytes_empty;
PyObject *const_tuple_empty;
PyObject *const_str_plain_rb;
PyObject *const_str_plain_end;
PyObject *const_str_plain_int;
PyObject *const_str_plain_len;
PyObject *const_str_plain_sum;
PyObject *const_str_plain_dict;
PyObject *const_str_plain_file;
PyObject *const_str_plain_iter;
PyObject *const_str_plain_keys;
PyObject *const_str_plain_name;
PyObject *const_str_plain_open;
PyObject *const_str_plain_read;
PyObject *const_str_plain_repr;
PyObject *const_str_plain_send;
PyObject *const_str_plain_site;
PyObject *const_str_plain_type;
PyObject *const_float_minus_0_0;
PyObject *const_str_plain_bytes;
PyObject *const_str_plain_close;
PyObject *const_str_plain_level;
PyObject *const_str_plain_print;
PyObject *const_str_plain_range;
PyObject *const_str_plain_throw;
PyObject *const_str_plain_tuple;
PyObject *const_str_plain_types;
PyObject *const_str_plain_format;
PyObject *const_str_plain_locals;
PyObject *const_str_plain___all__;
PyObject *const_str_plain___cmp__;
PyObject *const_str_plain___doc__;
PyObject *const_str_plain_compile;
PyObject *const_str_plain_globals;
PyObject *const_str_plain_inspect;
PyObject *const_str_plain___dict__;
PyObject *const_str_plain___exit__;
PyObject *const_str_plain___file__;
PyObject *const_str_plain___iter__;
PyObject *const_str_plain___main__;
PyObject *const_str_plain___name__;
PyObject *const_str_plain___path__;
PyObject *const_str_plain___spec__;
PyObject *const_str_plain_fromlist;
PyObject *const_str_plain___class__;
PyObject *const_str_plain___enter__;
PyObject *const_str_plain_bytearray;
PyObject *const_str_plain___cached__;
PyObject *const_str_plain___import__;
PyObject *const_str_plain___loader__;
PyObject *const_str_plain___module__;
PyObject *const_str_plain___getitem__;
PyObject *const_str_plain___package__;
PyObject *const_str_plain_classmethod;
PyObject *const_str_plain___builtins__;
PyObject *const_str_plain___compiled__;
PyObject *const_str_plain___internal__;
PyObject *const_str_plain_staticmethod;
PyObject *const_str_plain___metaclass__;
PyObject *const_str_plain__initializing;
PyObject *const_str_plain___mro_entries__;
PyObject *const_str_plain___class_getitem__;
PyObject *const_str_plain_submodule_search_locations;
PyObject *const_str_digest_25731c733fd74e8333aa29126ce85686;
PyObject *const_str_digest_2ba7f6302128d3d266d3c2da2c435ade;
PyObject *const_str_digest_45e4dde2057b0bf276d6a84f4c917d27;
PyObject *const_str_digest_9816e8d1552296af90d250823c964059;
PyObject *const_str_digest_adc474dd61fbd736d69c1bac5d9712e0;
PyObject *const_str_digest_b2daf4789816becfc0ef99630a60906a;
PyObject *const_tuple_anon_function_anon_builtin_function_or_method_tuple;

static void _createGlobalConstants( void )
{
    NUITKA_MAY_BE_UNUSED PyObject *exception_type, *exception_value;
    NUITKA_MAY_BE_UNUSED PyTracebackObject *exception_tb;

#ifdef _MSC_VER
    // Prevent unused warnings in case of simple programs, the attribute
    // NUITKA_MAY_BE_UNUSED doesn't work for MSVC.
    (void *)exception_type; (void *)exception_value; (void *)exception_tb;
#endif

    const_int_0 = PyLong_FromUnsignedLong( 0ul );
    const_str_dot = UNSTREAM_STRING_ASCII( &constant_bin[ 22 ], 1, 0 );
    const_float_0_0 = UNSTREAM_FLOAT( &constant_bin[ 37479 ] );
    const_int_pos_1 = PyLong_FromUnsignedLong( 1ul );
    const_str_empty = UNSTREAM_STRING_ASCII( &constant_bin[ 0 ], 0, 0 );
    const_dict_empty = _PyDict_NewPresized( 0 );
    assert( PyDict_Size( const_dict_empty ) == 0 );
    const_bytes_empty = UNSTREAM_BYTES( &constant_bin[ 0 ], 0 );
    const_tuple_empty = PyTuple_New( 0 );
    const_str_plain_rb = UNSTREAM_STRING_ASCII( &constant_bin[ 795 ], 2, 1 );
    const_str_plain_end = UNSTREAM_STRING_ASCII( &constant_bin[ 23 ], 3, 1 );
    const_str_plain_int = UNSTREAM_STRING_ASCII( &constant_bin[ 155 ], 3, 1 );
    const_str_plain_len = UNSTREAM_STRING_ASCII( &constant_bin[ 2574 ], 3, 1 );
    const_str_plain_sum = UNSTREAM_STRING_ASCII( &constant_bin[ 1794 ], 3, 1 );
    const_str_plain_dict = UNSTREAM_STRING_ASCII( &constant_bin[ 853 ], 4, 1 );
    const_str_plain_file = UNSTREAM_STRING_ASCII( &constant_bin[ 3672 ], 4, 1 );
    const_str_plain_iter = UNSTREAM_STRING_ASCII( &constant_bin[ 37487 ], 4, 1 );
    const_str_plain_keys = UNSTREAM_STRING_ASCII( &constant_bin[ 787 ], 4, 1 );
    const_str_plain_name = UNSTREAM_STRING_ASCII( &constant_bin[ 634 ], 4, 1 );
    const_str_plain_open = UNSTREAM_STRING_ASCII( &constant_bin[ 12203 ], 4, 1 );
    const_str_plain_read = UNSTREAM_STRING_ASCII( &constant_bin[ 992 ], 4, 1 );
    const_str_plain_repr = UNSTREAM_STRING_ASCII( &constant_bin[ 37491 ], 4, 1 );
    const_str_plain_send = UNSTREAM_STRING_ASCII( &constant_bin[ 284 ], 4, 1 );
    const_str_plain_site = UNSTREAM_STRING_ASCII( &constant_bin[ 7664 ], 4, 1 );
    const_str_plain_type = UNSTREAM_STRING_ASCII( &constant_bin[ 4298 ], 4, 1 );
    const_float_minus_0_0 = UNSTREAM_FLOAT( &constant_bin[ 37495 ] );
    const_str_plain_bytes = UNSTREAM_STRING_ASCII( &constant_bin[ 37503 ], 5, 1 );
    const_str_plain_close = UNSTREAM_STRING_ASCII( &constant_bin[ 82 ], 5, 1 );
    const_str_plain_level = UNSTREAM_STRING_ASCII( &constant_bin[ 26263 ], 5, 1 );
    const_str_plain_print = UNSTREAM_STRING_ASCII( &constant_bin[ 37508 ], 5, 1 );
    const_str_plain_range = UNSTREAM_STRING_ASCII( &constant_bin[ 5466 ], 5, 1 );
    const_str_plain_throw = UNSTREAM_STRING_ASCII( &constant_bin[ 37513 ], 5, 1 );
    const_str_plain_tuple = UNSTREAM_STRING_ASCII( &constant_bin[ 18788 ], 5, 1 );
    const_str_plain_types = UNSTREAM_STRING_ASCII( &constant_bin[ 37518 ], 5, 1 );
    const_str_plain_format = UNSTREAM_STRING_ASCII( &constant_bin[ 37523 ], 6, 1 );
    const_str_plain_locals = UNSTREAM_STRING_ASCII( &constant_bin[ 194 ], 6, 1 );
    const_str_plain___all__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37529 ], 7, 1 );
    const_str_plain___cmp__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37536 ], 7, 1 );
    const_str_plain___doc__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37543 ], 7, 1 );
    const_str_plain_compile = UNSTREAM_STRING_ASCII( &constant_bin[ 37550 ], 7, 1 );
    const_str_plain_globals = UNSTREAM_STRING_ASCII( &constant_bin[ 37557 ], 7, 1 );
    const_str_plain_inspect = UNSTREAM_STRING_ASCII( &constant_bin[ 1643 ], 7, 1 );
    const_str_plain___dict__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37564 ], 8, 1 );
    const_str_plain___exit__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37572 ], 8, 1 );
    const_str_plain___file__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37580 ], 8, 1 );
    const_str_plain___iter__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37588 ], 8, 1 );
    const_str_plain___main__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37596 ], 8, 1 );
    const_str_plain___name__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37604 ], 8, 1 );
    const_str_plain___path__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37612 ], 8, 1 );
    const_str_plain___spec__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37620 ], 8, 1 );
    const_str_plain_fromlist = UNSTREAM_STRING_ASCII( &constant_bin[ 37628 ], 8, 1 );
    const_str_plain___class__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37636 ], 9, 1 );
    const_str_plain___enter__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37645 ], 9, 1 );
    const_str_plain_bytearray = UNSTREAM_STRING_ASCII( &constant_bin[ 37654 ], 9, 1 );
    const_str_plain___cached__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37663 ], 10, 1 );
    const_str_plain___import__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37673 ], 10, 1 );
    const_str_plain___loader__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37683 ], 10, 1 );
    const_str_plain___module__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37693 ], 10, 1 );
    const_str_plain___getitem__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37703 ], 11, 1 );
    const_str_plain___package__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37714 ], 11, 1 );
    const_str_plain_classmethod = UNSTREAM_STRING_ASCII( &constant_bin[ 37725 ], 11, 1 );
    const_str_plain___builtins__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37736 ], 12, 1 );
    const_str_plain___compiled__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37748 ], 12, 1 );
    const_str_plain___internal__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37760 ], 12, 1 );
    const_str_plain_staticmethod = UNSTREAM_STRING_ASCII( &constant_bin[ 37772 ], 12, 1 );
    const_str_plain___metaclass__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37784 ], 13, 1 );
    const_str_plain__initializing = UNSTREAM_STRING_ASCII( &constant_bin[ 37797 ], 13, 1 );
    const_str_plain___mro_entries__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37810 ], 15, 1 );
    const_str_plain___class_getitem__ = UNSTREAM_STRING_ASCII( &constant_bin[ 37825 ], 17, 1 );
    const_str_plain_submodule_search_locations = UNSTREAM_STRING_ASCII( &constant_bin[ 37842 ], 26, 1 );
    const_str_digest_25731c733fd74e8333aa29126ce85686 = UNSTREAM_STRING_ASCII( &constant_bin[ 5428 ], 2, 0 );
    const_str_digest_2ba7f6302128d3d266d3c2da2c435ade = UNSTREAM_STRING_ASCII( &constant_bin[ 37868 ], 49, 0 );
    const_str_digest_45e4dde2057b0bf276d6a84f4c917d27 = UNSTREAM_STRING_ASCII( &constant_bin[ 1866 ], 7, 0 );
    const_str_digest_9816e8d1552296af90d250823c964059 = UNSTREAM_STRING_ASCII( &constant_bin[ 37917 ], 46, 0 );
    const_str_digest_adc474dd61fbd736d69c1bac5d9712e0 = UNSTREAM_STRING_ASCII( &constant_bin[ 37963 ], 47, 0 );
    const_str_digest_b2daf4789816becfc0ef99630a60906a = UNSTREAM_STRING_ASCII( &constant_bin[ 38010 ], 22, 0 );
    const_tuple_anon_function_anon_builtin_function_or_method_tuple = PyTuple_New( 2 );
    PyTuple_SET_ITEM( const_tuple_anon_function_anon_builtin_function_or_method_tuple, 0, (PyObject *)&PyFunction_Type ); Py_INCREF( (PyObject *)&PyFunction_Type );
    PyTuple_SET_ITEM( const_tuple_anon_function_anon_builtin_function_or_method_tuple, 1, (PyObject *)&PyCFunction_Type ); Py_INCREF( (PyObject *)&PyCFunction_Type );

#if _NUITKA_EXE
    /* Set the "sys.executable" path to the original CPython executable. */
    PySys_SetObject(
        (char *)"executable",
        const_str_digest_b2daf4789816becfc0ef99630a60906a
    );

#ifndef _NUITKA_STANDALONE
    /* Set the "sys.prefix" path to the original one. */
    PySys_SetObject(
        (char *)"prefix",
        const_str_digest_2ba7f6302128d3d266d3c2da2c435ade
    );

    /* Set the "sys.prefix" path to the original one. */
    PySys_SetObject(
        (char *)"exec_prefix",
        const_str_digest_2ba7f6302128d3d266d3c2da2c435ade
    );


#if PYTHON_VERSION >= 300
    /* Set the "sys.base_prefix" path to the original one. */
    PySys_SetObject(
        (char *)"base_prefix",
        const_str_digest_2ba7f6302128d3d266d3c2da2c435ade
    );

    /* Set the "sys.exec_base_prefix" path to the original one. */
    PySys_SetObject(
        (char *)"base_exec_prefix",
        const_str_digest_2ba7f6302128d3d266d3c2da2c435ade
    );

#endif
#endif
#endif

    static PyTypeObject Nuitka_VersionInfoType;

    // Same fields as "sys.version_info" except no serial number.
    static PyStructSequence_Field Nuitka_VersionInfoFields[] = {
        {(char *)"major", (char *)"Major release number"},
        {(char *)"minor", (char *)"Minor release number"},
        {(char *)"micro", (char *)"Micro release number"},
        {(char *)"releaselevel", (char *)"'alpha', 'beta', 'candidate', or 'release'"},
        {0}
    };

    static PyStructSequence_Desc Nuitka_VersionInfoDesc = {
        (char *)"__nuitka_version__",                                    /* name */
        (char *)"__compiled__\n\nVersion information as a named tuple.", /* doc */
        Nuitka_VersionInfoFields,                                        /* fields */
        4
    };

    PyStructSequence_InitType(&Nuitka_VersionInfoType, &Nuitka_VersionInfoDesc);

    Nuitka_dunder_compiled_value = PyStructSequence_New(&Nuitka_VersionInfoType);
    assert(Nuitka_dunder_compiled_value != NULL);

    PyStructSequence_SET_ITEM(Nuitka_dunder_compiled_value, 0, PyInt_FromLong(0));
    PyStructSequence_SET_ITEM(Nuitka_dunder_compiled_value, 1, PyInt_FromLong(6));
    PyStructSequence_SET_ITEM(Nuitka_dunder_compiled_value, 2, PyInt_FromLong(5));

#if PYTHON_VERSION < 300
    PyStructSequence_SET_ITEM(Nuitka_dunder_compiled_value, 3, PyString_FromString("release"));
#else
    PyStructSequence_SET_ITEM(Nuitka_dunder_compiled_value, 3, PyUnicode_FromString("release"));
#endif
    // Prevent users from creating the Nuitka version type object.
    Nuitka_VersionInfoType.tp_init = NULL;
    Nuitka_VersionInfoType.tp_new = NULL;


}

// In debug mode we can check that the constants were not tampered with in any
// given moment. We typically do it at program exit, but we can add extra calls
// for sanity.
#ifndef __NUITKA_NO_ASSERT__
void checkGlobalConstants( void )
{

}
#endif

void createGlobalConstants( void )
{
    if ( _sentinel_value == NULL )
    {
#if PYTHON_VERSION < 300
        _sentinel_value = PyCObject_FromVoidPtr( NULL, NULL );
#else
        // The NULL value is not allowed for a capsule, so use something else.
        _sentinel_value = PyCapsule_New( (void *)27, "sentinel", NULL );
#endif
        assert( _sentinel_value );

        _createGlobalConstants();
    }
}
