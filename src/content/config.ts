import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    pilier: z.enum(['IA Agentique', 'QSE', 'Convergence']),
    sources: z.array(
      z.object({
        name: z.string(),
        url: z.string().url(),
      })
    ).optional(),
    snacks: z.object({
      linkedin: z.object({
        hook: z.string(),
        takeaway: z.string(),
      }),
      x_thread: z.array(
        z.record(z.string(), z.string())
      ),
    }),
  }),
});

export const collections = { blog };
