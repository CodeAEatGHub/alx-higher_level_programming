#include "lists.h"

/**
 * get_dnodeint_at_index - prints list element
 *
 * @head: Head of the doubly linked list
 * @index: Required index
 *
 * Return: List
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *parse;
	unsigned int i = 0;

	parse = head;
	if (head == NULL)
		return (NULL);
	while (parse->next != NULL)
	{
		if (i == index)
			return (parse);
		i++;
		parse = parse->next;
	}
	return (NULL);
}
