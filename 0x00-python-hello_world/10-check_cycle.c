#include "lists.h"
/**
 * check_cycle - checks if a list is a circular list
 * @list: list
 * Return: 0 || 1
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr = NULL;

	ptr = list;
	if (list)
	{
		while (ptr->next)
		{
			if (ptr->next == list)
				return (1);
			ptr = ptr->next;
		}
	}
	return (0);
}
