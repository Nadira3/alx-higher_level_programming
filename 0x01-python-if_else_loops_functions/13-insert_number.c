#include "lists.h"
/**
 * insert_node - inserts a node
 * @head: head of node
 * @number: number to be inserted
 * Return: pointer to head
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = NULL, *node = NULL;

	if (!head)
		return (NULL);
	ptr = *head;
	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;
	node->next = NULL;
	if (!*head || ptr->n > number)
	{
		node->next = *head;
		*head = node;
	}
	else
	{
		while (ptr->next && (ptr->next)->n < node->n)
			ptr = ptr->next;
		node->next = ptr->next;
		ptr->next = node;
	}
	return (*head);

}
