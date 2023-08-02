#include <Python.h>

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
	bits = (PyBytesObject*)p;
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
 * print_python_list_info - Prints basic information about a Python list
 * @p: The Python list to analyze
 *
 * Return: None
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, n;
	PyObject **item, *element;
	PyListObject *list = (PyListObject*)p;
	Py_ssize_t allocated = list->allocated;

	n = list->ob_size;
	if (n < 0)
		return;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", n);
	printf("[*] Allocated = %ld\n", allocated);
	for (i = 0; i < n; i++)
	{
		item = list->ob_items;
		element = item[i];
		if (!item)
			break;
		printf("Element %ld: %s\n", i, element->ob_type->tp_name);
		if (PyBytes_Check(element))
			print_python_bytes(element);
	}
}
