#include "lists.h"

/**
 * free_dlistint - prints list element
 *
 * @head: Head of the doubly linked list
 *
 * Return: Size of list
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *p1, *p2;

	p1 = p2 = head;
	while (p1->next != NULL)
	{
		p2 = p1;
		p1 = p1->next;
	}
	while (p2->prev != NULL)
	{
		free(p1);
		p1 = p2;
		p2 = p2->prev;
	}
	free(p2->next);
	free(p2);
}
