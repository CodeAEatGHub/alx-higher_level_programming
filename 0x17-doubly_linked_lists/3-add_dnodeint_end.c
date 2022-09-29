#include "lists.h"

/**
 * add_dnodeint_end - prints list element
 *
 * @head: Pointer to the head of the doubly linked list
 * @n: Element to be added
 *
 * Return: List
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *parse, *tmp;

	tmp = (dlistint_t *)(*head);
	parse = malloc(sizeof(dlistint_t));
	if (*head == NULL)
	{
		parse->n = n;
		parse->prev = NULL;
		parse->next = NULL;
		*head = parse;
		return (*head);
	}
	while (tmp->next != NULL && *head != NULL)
		tmp = tmp->next;
	parse->n = n;
	parse->next = NULL;
	parse->prev = tmp;
	/*parse->next->prev = parse;*/
	tmp->next = parse;
	/*printf("%d\n", parse->prev->n);*/
	return (parse);
}
