#include <Python.h>
#include <float.h>

/**
 * print_python_float - Prints basic information about a Python float object
 * @p: The Python float object to analyze
 *
 * Return: None
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *bits;

	bits = (PyFloatObject *)p;
	printf("[.] float object info\n");
	if (PyFloat_Check(bits))
		printf("  value: %.*g\n", DBL_DIG, bits->ob_fval);
	else
		printf("  [ERROR] Invalid Float Object\n");
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
	char *ptr = NULL;

	printf("[.] bytes object info\n");
	bits = (PyBytesObject *)p;
	if (PyBytes_Check(bits))
	{
		n = bits->ob_base.ob_size;
		ptr = bits->ob_sval;
		printf("  size: %ld\n", n);
		ptr[n] = 0;
		printf("  trying string: %s\n", ptr);
		printf("  first %ld bytes:", n < 10 ? n + 1 : 10);
		for (i = 0; i < (n < 10 ? n + 1 : 10); i++, ptr++)
			printf(" %.2x", *ptr);
		puts("");

	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}

/**
 * print_python_list - Prints basic information about a Python list
 * @p: The Python list to analyze
 *
 * Return: None
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, n;
	PyObject **item, *element;
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t allocated;

	printf("[*] Python list info\n");
	if (PyList_Check(list))
	{
		n = PyList_GET_SIZE(p);
		if (n < 0)
			return;
		allocated = list->allocated;
		printf("[*] Size of the Python List = %ld\n", n);
		printf("[*] Allocated = %ld\n", allocated);
		for (i = 0; i < n; i++)
		{
			item = list->ob_item;
			element = item[i];
			if (!item)
				break;
			printf("Element %ld: %s\n", i, element->ob_type->tp_name);
			if (PyBytes_Check(element))
				print_python_bytes(element);
			if (PyFloat_Check(element))
				print_python_float(element);
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
