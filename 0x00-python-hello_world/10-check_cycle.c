#include "lists.h"
/**
 * check_cycle - checks if a list is a circular list
 * @list: list
 * Return: 0 || 1
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr = NULL, *ptr2 = NULL;

	ptr = list;
	ptr2 = list;
	if (list)
	{
		while (ptr->next && ptr2->next->next)
		{
			ptr = ptr->next;
			ptr2 = ptr2->next->next;
			if (ptr == ptr2)
				return (1);
		}
	}
	return (0);
}
