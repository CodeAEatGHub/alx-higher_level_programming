#include "lists.h"

/**
 * add_dnodeint - prints list element
 *
 * @head: Head of the doubly linked list
 * @n: Element to be added
 *
 * Return: Size of list
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *parse;

	parse = malloc(sizeof(dlistint_t));
	if (head == NULL)
		return (NULL);
	parse->n = n;
	parse->next = *head;
	parse->prev = NULL;
	/*parse->next->prev = parse;*/
	*head = parse;
	parse = (*head)->next;
	/*printf("%d\n", parse->prev->n);*/
	return (parse);
}
