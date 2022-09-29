#include "lists.h"

/**
 * delete_dnodeint_at_index - prints list element
 *
 * @head: Head of the doubly linked list
 * @index: Required index
 *
 * Return: 1 if success
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *parse;
	unsigned int i = 0;

	if (*head == NULL)
		return (-1);
	parse = *head;
	while (parse != NULL)
	{
		if (i == index)
		{
			if (index != 0)
			{
				parse->prev->next = parse->next;
				parse->next->prev = parse->prev;
			}
			else
				*head = parse->next;
			free(parse);
			return (1);
		}
		i++;
		parse = parse->next;
	}
	return (-1);
}
