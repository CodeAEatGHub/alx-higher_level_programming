#include "lists.h"

/**
 * print_dlistint - prints list element
 *
 * @h: Head of the doubly linked list
 *
 * Return: Size of list
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;
	dlistint_t *parse;

	parse = (dlistint_t *)h;
	if (h == NULL)
		return (0);
	while (parse != NULL)
	{
		printf("%d\n", parse->n);
		parse = parse->next;
		count++;
	}
	return (count);
}
