#include "lists.h"

/**
 * insert_dnodeint_at_index - prints list element
 *
 * @h: Head of the doubly linked list
 * @idx: Index required
 * @n: Value to be inserted
 *
 * Return: Size of list
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *parse, *ins;
	unsigned int i = 0;

	ins = malloc(sizeof(dlistint_t));
	parse = *h;
	if (*h == NULL && idx == 0)
	{
		ins->n = n;
		ins->next = NULL;
		ins->prev = NULL;
		*h = ins;
	}
	while (parse->next != NULL)
	{
		if (i == idx)
		{
			ins->n = n;
			ins->prev = parse->prev;
			ins->next = parse;
			parse->prev->next = ins;
			parse->prev = ins;
			return (ins);
		}
		i++;
		parse = parse->next;
	}
	return (NULL);
}
