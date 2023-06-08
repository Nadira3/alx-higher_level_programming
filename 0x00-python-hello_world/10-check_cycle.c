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
		while (ptr->next && ptr2)
		{
			ptr2 = ptr->next->next;
			if (ptr->next == list || ptr->next == ptr2)
				return (1);
			ptr = ptr->next;
		}
	}
	return (0);
}
