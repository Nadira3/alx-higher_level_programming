#include "lists.h"
/**
 * check_cycle - checks if a list is a circular list
 * @list: list
 * Return: 0 || 1
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr = NULL;
	listint_t *prev = NULL;
	listint_t *new = NULL;
	int flag = 0;

	ptr = list;
	prev = list;
	new = list->next;
	if (list)
	{
		while (ptr->next)
		{
			if (((ptr == list) && flag) || ((ptr == prev) && flag) || ptr == new)
				return (1);
			ptr = ptr->next;
			if (flag)
				prev = prev->next;
			new = new->next;
			flag++;
		}
		return (0);
	}
	return (0);
}
