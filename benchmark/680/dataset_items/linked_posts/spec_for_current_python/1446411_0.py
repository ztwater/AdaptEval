Py_UNICODE
PyUnicode_GetMax(void)
{
#ifdef Py_UNICODE_WIDE
    return 0x10FFFF;
#else
    /* This is actually an illegal character, so it should
       not be passed to unichr. */
    return 0xFFFF;
#endif
}
