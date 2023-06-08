#include "lists.h"
/*
 *
 * int iscycle(listint_t *node, int n, listint_t *list)
 * {
 *	listint_t *ptr = NULL;
 *	int i = 0;
 *
 *	ptr = list;
 *	while (i < n && ptr->next)
 *	{
 *		i++;
 *		ptr = ptr->next;
 *		if (ptr->next == node->next && i < n && ptr != list)
 *			return (1);
 *	}
 *	return (0);
 *  } this was my previous solution. it works but its very slow. youll see this later and laugh. lol
 *  anyway's i had to learn the floyd's algorithm to solve this task.
 * int check_cycle(listint_t *list)
 * {
 *	listint_t *ptr = NULL;
 *	int i = 0;
 *
 *	ptr = list;
 *	if (list)
 *	{
 *		while (ptr->next)
 *		{
 *			if (ptr->next == list || iscycle(ptr, i, list))
 *				return (1);
 *			ptr = ptr->next;
 *			i++;
 *		}
 *	}
 *	return (0);
 * }
 */


/**
 * check_cycle - checks if a list is a circular list
 * @list: list
 * Return: 0 || 1
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr, *ptr2;

	ptr = list;
	ptr2 = list;
	if (list)
	{
		while (ptr2 && ptr2->next)
		{
			ptr = ptr->next;
			ptr2 = ptr2->next->next;
			if (ptr == ptr2)
				return (1);
		}
	}
	return (0);
}
