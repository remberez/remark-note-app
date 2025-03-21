import { api } from ".";

class NoteService {
    static async fetchMyNotes() {
        try {
            const response = await api.get("/notes/my");
            return response.data;
        } catch (error) {
            console.error(error);
        }
    }

    static async fetchDetailNote(noteId) {
        try {
            const response = await api.get(`/notes/${noteId}`);
            return response.data;
        } catch (error) {
            console.error(error);
        }
    }

    static async updateNote(noteData, noteId) {
        try {
            const resposne = await api.patch(`/notes/${noteId}`, noteData);
            return resposne.status;
        } catch (error) {
            console.error(error);
        }
    }

    static async createNote() {
        try {
            const response = await api.post("/notes/", {title: "Новая заметка", text: ""});
            return response;
        } catch (error) {
            console.error(error);
        }
    }

    static async deleteNote(noteId) {
        try {
            const response = await api.delete(`/notes/${noteId}/`);
            return response.status;
        } catch (error) {
            console.error(error);
        }
    }
}

export default NoteService;