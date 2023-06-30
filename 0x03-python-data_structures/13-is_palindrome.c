#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to head of list
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *pam = NULL, *pal = NULL, *f;
	listint_t *ptr1 = NULL, *ptr2 = NULL, *ptr3 = NULL;
	int len = 0;

	if (!head)
		return (0);
	pal = *head;
	pam = *head;

	while (pal && pal->next)
	{
		if (!(pal->next->next))
		{
			pal = pal->next;
			len += 1;
			break;
		}
		pam = pam->next;
		pal = pal->next->next;
		len += 2;
	}
	len += *head ? 1 : 0;
	/* at this point pam is at the middle of the list */
	if (len)
	{
		pal = *head;
		ptr1 = pam;
		ptr2 = pam->next;
		while (ptr2)
		{
			ptr3 = ptr2->next;
			ptr2->next = ptr1;
			ptr1 = ptr2;
			ptr2 = ptr3;
		}
		ptr2 = ptr1;
		pam->next = NULL;
		while (len % 2? pal->next : pal)
		{
			if (ptr1->n != pal->n)
			{
				while (ptr1->next)
				{
					f = ptr1;
					ptr1 = ptr1->next;
					free(f);
				}
				return (0);
			}
			ptr1 = ptr1->next;
			free(ptr2);
			ptr2 = ptr1;
			pal = pal->next;
		}
	}
	return (1);
}
