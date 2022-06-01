#include "lists.h"

/**
 * insert_node - insert a node to a list
 * head: head of the list
 * number: data of the list
 * Return: the address of the new node, or 
 * NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new_node;

	current = *head;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if ((current)->n >= number || current == NULL)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}
	while (current && current->next && current->next->n < new_node->n)
	{
		current = current->next;
	}
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
