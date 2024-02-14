#include <Python.h>
/**
  * fput_method - A wrapper for fputs function
  * @self: A redirect to the method itself.
  * @args: The array of arguments coming from python.
  *
  * Return: The number of byte written by fputs
  */
static PyObject *fput_method(PyObject *self, PyObject *args)
{
        /* Declare all argument to receive from python code */
        char *str, *filename = NULL;
        /*Declare other argument to be used here too*/
        int r;
        FILE *fp;

        /* Parse the arguments into local variables */
        if (!PyArg_ParseTuple(args, "ss", &str, &filename))
                return (NULL);
        fp = fopen(filename, "w");
        r = fputs("Insert this string\n", fp);
        fclose(fp);

        return (PyLong_FromLong(r));
}

/**
  * fputMethodArray An array of method definition in fputs.
  * Format is "calling_name", "func_name", "ArgsCount", "Docs"
  * 
  */
static PyMethodDef fputMethodArray[] = {
	{"fputs", fput_method, METH_VARARGS, "Fput docs"},
	{NULL, NULL, 0, NULL}
};

/**
  * struct fputModuleDef - The module definition
  * @PyModuleDef_HEAD_INIT: Initializes the function.
  * @fputs: Name by which user will call our function.
  *
  */
static struct PyModuleDef fputModuleDef = {
	PyModuleDef_HEAD_INIT,
	"fputs",
	"fput doc",
	-1,
	fputMethodArray
};

PyMODINIT_FUNC PyInit_fputs(void)
{
	return PyModule_Create(&fputModuleDef);
}
