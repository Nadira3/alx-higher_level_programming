#include <Python.h>

/**
 * print_python_list_info - Prints basic information about a Python list
 * @p: The Python list to analyze
 *
 * Return: None
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, n;
	PyObject *item;
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	n = PyList_Size(p);
	if (n < 0)
		return;
	printf("[*] Size of the Python List = %ld\n", n);
	printf("[*] Allocated = %ld\n", allocated);
	for (i = 0; i < n; i++)
	{
		item = PyList_GetItem(p, i);
		if (!item)
			break;
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - Prints basic information about a Python object
 * @p: The Python object to analyze
 *
 * Return: None
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, n;
	PyBytesObject *bits;

	printf("[.] bytes object info\n");
	bits = (PyBytesObject*)p;
	if (PyBytes_Check(bits))
		printf("  size: %ld\n", bits->PyObject_VAR_HEAD.ob_size);
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}
