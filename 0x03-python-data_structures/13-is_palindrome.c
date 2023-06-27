#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to head of list
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *pam, *pal;
	int list_len = 0, i, j = 0, len;

	if (!head)
		return (0);
	pal = *head;
	pam = *head;

	while (pal && pal->next)
	{
		if (!(pal->next->next))
		{
			pal = pal->next;
			break;
		}
		pam = pam->next;
		pal = pal->next->next;
	}
	/* at this point pam is at the middle of the list */
	printf("pal->n: %d, pam->next: %d\n", pal->n, pam->n);
}
