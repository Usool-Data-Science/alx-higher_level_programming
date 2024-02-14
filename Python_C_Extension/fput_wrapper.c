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
	if (!PyArg_parseList(args, "ss", &str, &filename))
		return (NULL);
	fp = fopen(filename, "w");
	r = fputs("Insert this string\n", fp);
	fclose(fp);

	return (PyLong_FromLong r);
}
