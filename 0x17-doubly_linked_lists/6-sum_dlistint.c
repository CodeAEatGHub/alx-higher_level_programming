#include "lists.h"

/**
 * sum_dlistint - prints list element
 *
 * @head: Head of the doubly linked list
 *
 * Return: Sum of list
 */
int sum_dlistint(dlistint_t *head)
{
	dlistint_t *parse;
	int sum = 0;

	parse = head;
	if (head == NULL)
		return (0);
	while (parse != NULL)
	{
		printf("%d", parse->n);
		sum += parse->n;
		parse = parse->next;
	}
	return (sum);
}
