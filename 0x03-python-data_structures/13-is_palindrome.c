#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to head of list
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr, *pal;
	int list_len = 0, i, j = 0, len;

	if (!head)
		return (0);
	pal = *head;
	ptr = *head;

	while (ptr)
	{
		ptr = ptr->next;
		list_len++;
	}
	ptr = *head;
	len = list_len;
	for (i = 0; i < (list_len % 2 == 0 ? list_len / 2 : list_len / 2 + 1); i++)
	{
		while (j++ < len - 1)
			pal = pal->next;
		if (ptr->n != pal->n)
			return (0);
		printf("i: %d, list_len: %d, ptr->n: %d, pal->n: %d\n", i, list_len / 2, ptr->n, pal->n);
		len--;
		ptr = ptr->next;
		pal = *head;
		j = 0;
	}
	return (1);
}
