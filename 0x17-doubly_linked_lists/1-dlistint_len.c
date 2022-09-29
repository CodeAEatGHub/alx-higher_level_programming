#include "lists.h"

/**
 * dlistint_len - prints list element
 *
 * @h: Head of the doubly linked list
 *
 * Return: Size of list
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t count = 0;
	dlistint_t *parse;

	if (h == NULL)
		return (0);
	parse = (dlistint_t *)h;
	while (parse != NULL)
	{
		parse = parse->next;
		count++;
	}
	return (count);
}
