#include "lists.h"

/**
 * is_palindrome - Checks if a list is palindrome
 *
 * @head: Address of pointer to the head of the list
 *
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t  *end_parser = *head;
	int i = 0, j = 0, *p;

	if (head == NULL)
		return (1);
	while (end_parser != NULL)
	{
		i++;
		if (end_parser->next == NULL)
			break;
		end_parser = end_parser->next;
	}
	p = malloc(sizeof(int) * i);
	end_parser = *head;
	for (j = 0 ; j < i ; j++)
	{
		p[j] = end_parser->n;
		end_parser = end_parser->next;
	}
	for (j = 0 ; j < i ; j++)
	{
		if (p[j] != p[i - 1 - j])
			return (0);
	}
	free(p);
	return (1);
}
