#include "lists.h"
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
	for (i = 0; i < (list_len / 2) - 1; i++)
	{
		while (j++ < len - 1)
			pal = pal->next;
		if (ptr->n != pal->n)
			return (0);
		len--;
		ptr = ptr->next;
		pal = *head;
		j = 0;
	}
	return (1);
}

int main(void)
{
	listint_t *new = NULL;
	int x = is_palindrome(&new);
	printf("%d\n", x);
}
