#include "lists.h"
/**
 * check_cycle - checks if a list is a circular list
 * @list: list
 * Return: 0 || 1
 */
int iscycle(listint_t *node, int n, listint_t *list)
{
	listint_t *ptr = NULL;
	int i = 0;

	ptr = list;
	while (i < n && ptr->next)
	{
		i++;
		ptr = ptr->next;
		if (ptr->next == node->next && i < n && ptr != list)
			return (1);
	}
	return (0);
}
int check_cycle(listint_t *list)
{
	listint_t *ptr = NULL;
	int i = 0;

	ptr = list;
	if (list)
	{
		while (ptr->next)
		{
			if (ptr->next == list || iscycle(ptr, i, list))
				return (1);
			ptr = ptr->next;
			i++;
		}
	}
	return (0);
}
