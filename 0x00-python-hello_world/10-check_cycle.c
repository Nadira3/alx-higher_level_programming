#include "lists.h"
/**
 * check_cycle - checks if a list is a circular list
 * @list: list
 * Return: 0 || 1
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr = NULL;

	if (!list)
		return (0);
	ptr = list;
	do {
		ptr = ptr->next;
		if (ptr == list)
			break;
		if (!ptr)
			return (0);
	} while (1);
	return (1);
}
