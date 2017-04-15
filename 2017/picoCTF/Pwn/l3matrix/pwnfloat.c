#include <python2.7/Python.h>


static PyObject *
pwnfloat_unpackfloat(PyObject *self, PyObject *args)
{
  char *c,*t;
  float r;
  int i,s;
  
  if (!PyArg_ParseTuple(args, "s#", &c,&s))
    return NULL;
  t = (char *) (&r);
    for (i=0;i<sizeof(float);i++) t[i]=c[i];
    return Py_BuildValue("f", r);
}

static PyObject *
pwnfloat_packfloat(PyObject *self, PyObject *args)
{
    float r;
    char *s;
    char t[]="abcd\x00";
    int i;
    
    if (!PyArg_ParseTuple(args, "f", &r))
        return NULL;
    s=(char *) (&r);
    for (i=0;i<sizeof(float);i++) t[i]=s[i];
    return Py_BuildValue("s#", t,sizeof(float));
}

static PyMethodDef PwnfloatMethods[] = {
    {"packfloat",  pwnfloat_packfloat, METH_VARARGS,
     "Float to string."},
    {"unpackfloat",  pwnfloat_unpackfloat, METH_VARARGS,
     "String to float."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};


PyMODINIT_FUNC
initpwnfloat(void)
{
    (void) Py_InitModule("pwnfloat", PwnfloatMethods);
}
